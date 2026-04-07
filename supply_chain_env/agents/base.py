from typing import Any, Dict, Optional


class BaseAgent:
    def __init__(self, name: str):
        self.name = name
        self.env = None
        self.last_action = None
        self.metrics = {
            'stockouts': 0,
            'orders': 0,
            'demand_history': [],
        }

    def initialize(self, env: Any = None) -> None:
        self.env = env
        self.reset()

    def reset(self) -> None:
        self.last_action = None
        self.metrics = {
            'stockouts': 0,
            'orders': 0,
            'demand_history': [],
        }

    def normalize_observation(self, observation: Any) -> Dict[str, Any]:
        if observation is None:
            return {}
        if isinstance(observation, dict):
            return observation
        if hasattr(observation, 'to_dict'):
            return observation.to_dict()
        if hasattr(observation, 'inventory') and hasattr(observation, 'demand'):
            return {
                'inventory': getattr(observation, 'inventory', 0),
                'demand': getattr(observation, 'demand', 0),
            }
        return {}

    def act(self, observation: Dict[str, Any]) -> str:
        raise NotImplementedError

    def update(self, action: str, reward: Any, info: Dict[str, Any]) -> None:
        self.last_action = action
        self.metrics['orders'] += 1
        self.metrics['demand_history'].append(info.get('demand', 0))
        if info.get('sold', 0) < info.get('demand', 0):
            self.metrics['stockouts'] += 1
