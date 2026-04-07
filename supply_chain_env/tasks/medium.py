from env.environment import SupplyChainEnv


class Medium:
    def __init__(self):
        self.env = SupplyChainEnv()
        self.steps = self.env.max_steps

    def run(self):
        self.env.reset()
        stockouts = 0
        excess_inventory = 0
        total_steps = 0

        for _ in range(self.steps):
            state = self.env.state()
            if state.inventory < 400:
                action = 'order_large'
            elif state.inventory > 1000:
                action = 'do_nothing'
            else:
                action = 'order_small'

            observation, reward, done, info = self.env.step(action)
            if isinstance(observation, dict):
                inv = observation.get('inventory', 0)
            else:
                inv = observation.inventory
            
            if info.get('demand', 0) > info.get('sold', 0):
                stockouts += 1
            excess_inventory += max(0, inv - 900)
            total_steps += 1

            if done:
                break

        return {
            'task': 'medium',
            'steps': total_steps,
            'stockouts': stockouts,
            'excess_inventory': excess_inventory,
            'final_inventory': self.env.state().inventory,
            'final_money': self.env.state().money,
        }
