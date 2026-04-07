from env.environment import SupplyChainEnv


class Medium:
    def __init__(self):
        self.env = SupplyChainEnv()
        self.steps = self.env.max_steps

    def run(self):
        state = self.env.reset()
        stockouts = 0
        excess_inventory = 0

        for _ in range(self.steps):
            if state.inventory < 400:
                action = 'order_large'
            else:
                action = 'order_small'

            observation, reward, done, info = self.env.step(action)
            if info['demand'] > info['sold']:
                stockouts += 1
            excess_inventory += max(0, observation['inventory'] - 900)
            state = self.env.state()

            if done:
                break

        return {
            'task': 'medium',
            'steps': self.env.current_step,
            'stockouts': stockouts,
            'excess_inventory': excess_inventory,
            'final_inventory': state.inventory,
        }
