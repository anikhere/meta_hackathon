from .employee_agent import EmployeeAgent
from .forecasting_agent import ForecastingAgent
from .inventory_agent import InventoryAgent
from .management_agent import ManagementAgent
from env.environment import SupplyChainEnv


def initialize_agents():
    return [
        EmployeeAgent(),
        ForecastingAgent(),
        InventoryAgent(),
        ManagementAgent(),
    ]


class AgentManager:
    def __init__(self, env_cls=SupplyChainEnv):
        self.env_cls = env_cls
        self.agents = []

    def initialize(self):
        self.agents = initialize_agents()
        return self.agents

    def run_all(self, steps=None):
        results = []
        for agent in self.initialize():
            env = self.env_cls()
            observation = env.reset()
            agent.initialize(env)
            total_reward = 0.0
            for _ in range(steps or env.max_steps):
                action = agent.act(observation)
                observation, reward, done, info = env.step(action)
                agent.update(action, reward, info)
                total_reward += reward[0] if isinstance(reward, tuple) else reward
                if done:
                    break
            results.append({
                'agent': agent.name,
                'steps': env.current_step,
                'final_money': env.state().money,
                'total_reward': total_reward,
                'metrics': agent.metrics,
            })
        return results
