from env.environment import SupplyChainEnv


class Hard:
    def __init__(self):
        self.env = SupplyChainEnv()
        self.steps = self.env.max_steps

    def run(self):
        self.env.reset()
        total_reward = 0.0

        for _ in range(self.steps):
            state = self.env.state()
            if state.inventory < 300:
                action = 'order_large'
            else:
                action = 'order_small'

            observation, reward, done, info = self.env.step(action)
            total_reward += reward[0] if isinstance(reward, tuple) else reward

            if done:
                break

        final_money = self.env.state().money
        return {
            'task': 'hard',
            'steps': self.env.current_step,
            'total_reward': total_reward,
            'final_money': final_money,
        }
