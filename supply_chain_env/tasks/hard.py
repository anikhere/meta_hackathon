from env.environment import SupplyChainEnv


class Hard:
    def __init__(self):
        self.env = SupplyChainEnv()
        self.steps = self.env.max_steps

    def run(self):
        self.env.reset()
        total_reward = 0.0
        total_steps = 0

        for _ in range(self.steps):
            state = self.env.state()
            if state.inventory < 300:
                action = 'order_large'
            elif state.money > 15000:
                action = 'do_nothing'
            else:
                action = 'order_small'

            observation, reward, done, info = self.env.step(action)
            reward_val = reward[0] if isinstance(reward, tuple) else reward
            total_reward += reward_val
            total_steps += 1

            if done:
                break

        final_money = self.env.state().money
        return {
            'task': 'hard',
            'steps': total_steps,
            'total_reward': total_reward,
            'final_money': final_money,
            'profit': final_money - 10000,
        }
