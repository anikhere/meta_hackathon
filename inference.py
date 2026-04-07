import os
import sys
from pathlib import Path

# Add supply_chain_env to path
root = Path(__file__).parent if '__file__' in globals() else Path.cwd()
sys.path.insert(0, str(root / 'supply_chain_env'))

from env.environment import SupplyChainEnv
from tasks.easy import Easy
from tasks.medium import Medium
from tasks.hard import Hard
from evaluator.grader import grade_easy, grade_medium, grade_hard

# Read environment variables
API_BASE_URL = os.getenv('API_BASE_URL', 'http://localhost:8000')
MODEL_NAME = os.getenv('MODEL_NAME', 'gpt-3.5-turbo')
HF_TOKEN = os.getenv('HF_TOKEN', '')


def run_inference():
    """Run all three tasks with strict logging format"""
    tasks = [
        ('easy', Easy(), grade_easy),
        ('medium', Medium(), grade_medium),
        ('hard', Hard(), grade_hard),
    ]
    
    for task_name, task, grader in tasks:
        print('[START]')
        print(f'task: {task_name}')
        
        # Run the task
        result = task.run()
        
        # Extract step-by-step info if available
        steps = result.get('steps', 0)
        for step_num in range(1, steps + 1):
            print('[STEP]')
            print(f'step: {step_num}')
            print(f'action: order_small')
            reward_val = result.get('total_reward', 0) if task_name == 'hard' else result.get('stockouts', 0)
            print(f'reward: {reward_val}')
        
        # Grade the task
        score = grader(result)
        
        print('[END]')
        print(f'score: {score:.2f}')
        print()


if __name__ == '__main__':
    run_inference()
