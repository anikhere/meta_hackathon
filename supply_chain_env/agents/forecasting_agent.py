from env.action import ORDER_SMALL, ORDER_LARGE
from .base import BaseAgent


class ForecastingAgent(BaseAgent):
    def __init__(self, window: int = 5):
        super().__init__('forecasting_agent')
        self.window = window

    def act(self, observation):
        observation = self.normalize_observation(observation)
        demand_history = self.metrics['demand_history']
        if demand_history:
            forecast = int(sum(demand_history[-self.window:]) / len(demand_history[-self.window:]) + 0.5)
        else:
            forecast = observation.get('demand', 10)

        target_inventory = forecast + 150
        inventory = observation.get('inventory', 0)
        return ORDER_LARGE if inventory < target_inventory else ORDER_SMALL
