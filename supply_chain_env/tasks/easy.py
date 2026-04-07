from env.environment import SupplyChainEnv


class Easy:
    def __init__(self):
        self.env = SupplyChainEnv()
        self.steps = self.env.max_steps

    def run(self):
        state = self.env.reset()
        stockouts = 0
        total_demand = 0
        total_sold = 0

        for _ in range(self.steps):
            if state.inventory < 600:
                action = 'order_small'
            elif state.inventory < 900:
                action = 'order_large'
            else:
                action = 'order_small'

            observation, reward, done, info = self.env.step(action)
            demand = info['demand']
            sold = info['sold']
            total_sold += sold
            total_demand += demand
            if demand > sold:
                stockouts += 1
            state = self.env.state()

            if done:
                break

        return {
            'task': 'easy',
            'steps': self.env.current_step,
            'stockouts': stockouts,
            'total_demand': total_demand,
            'total_sold': total_sold,
        }


            
