from env.action import ORDER_SMALL, ORDER_LARGE
from .base import BaseAgent


class EmployeeAgent(BaseAgent):
    def __init__(self):
        super().__init__('employee_agent')

    def act(self, observation):
        observation = self.normalize_observation(observation)
        inventory = observation.get('inventory', 0)
        if inventory < 450:
            return ORDER_LARGE
        if inventory > 1200:
            return ORDER_SMALL
        return ORDER_SMALL
