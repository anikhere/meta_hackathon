from env.action import ORDER_SMALL, ORDER_LARGE
from .base import BaseAgent


class ManagementAgent(BaseAgent):
    def __init__(self):
        super().__init__('management_agent')

    def act(self, observation):
        observation = self.normalize_observation(observation)
        inventory = observation.get('inventory', 0)
        demand = observation.get('demand', 0)
        if inventory < demand * 2 or inventory < 400:
            return ORDER_LARGE
        return ORDER_SMALL
