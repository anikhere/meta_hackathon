import os
import sys
from pathlib import Path
from openai import OpenAI

root = Path(__file__).parent
sys.path.insert(0, str(root / 'supply_chain_env'))

from env.environment import SupplyChainEnv
from evaluator.grader import grade_easy, grade_medium, grade_hard

API_BASE_URL = os.environ.get('API_BASE_URL', 'https://api-inference.huggingface.co/v1')
MODEL_NAME = os.environ.get('MODEL_NAME', 'mistralai/Mistral-7B-Instruct-v0.3')
HF_TOKEN = os.environ.get('HF_TOKEN', '')

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN if HF_TOKEN else "dummy",
)

SYSTEM_PROMPT = """You are a supply chain agent. Reply with ONLY one of: order_small, order_large, do_nothing"""

def get_llm_action(inventory, demand):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            max_tokens=10,
            temperature=0.0,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"inventory={inventory}, demand={demand}. Action?"}
            ]
        )
        action = response.choices[0].message.content.strip().lower()
        if action not in ("order_small", "order_large", "do_nothing"):
            action = "order_small"
        return action
    except Exception:
        if inventory < 500:
            return "order_large"
        elif inventory < 900:
            return "order_small"
        return "do_nothing"

def run_task(task_name, grader):
    env = SupplyChainEnv()
    env.reset()
    print("[START]")
    print(f"task: {task_name}")
    stockouts = 0
    excess_inventory = 0
    total_reward = 0.0
    step_num = 0
    while True:
        state = env.state()
        action = get_llm_action(state.inventory, state.demand)
        observation, reward, done, info = env.step(action)
        step_num += 1
        reward_val = float(reward)
        total_reward += reward_val
        if info.get('demand', 0) > info.get('sold', 0):
            stockouts += 1
        inv = observation.get('inventory', 0) if isinstance(observation, dict) else observation.inventory
        excess_inventory += max(0, inv - 900)
        print("[STEP]")
        print(f"step: {step_num}")
        print(f"action: {action}")
        print(f"reward: {reward_val:.4f}")
        if done:
            break
    result = {'steps': step_num, 'stockouts': stockouts, 'excess_inventory': excess_inventory, 'profit': env.state().money - 10000, 'total_reward': total_reward}
    score = grader(result)
    print("[END]")
    print(f"score: {score:.4f}")
    print()

if __name__ == '__main__':
    run_task('easy', grade_easy)
    run_task('medium', grade_medium)
    run_task('hard', grade_hard)
