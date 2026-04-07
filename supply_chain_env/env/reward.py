class Reward:
    def __init__(self, sold, demand, inventory):
        self.sold = sold
        self.demand = demand
        self.inventory = inventory

    def compute_reward(self, price):
        # profit
        profit = self.sold * price

        # holding cost (too much inventory)
        holding_penalty = self.inventory * 0.1

        # stockout penalty (missed demand)
        stockout_penalty = max(0, self.demand - self.sold) * 5

        # final reward
        reward = profit - holding_penalty - stockout_penalty

        return reward, {
    "profit": profit,
    "holding_penalty": holding_penalty,
    "stockout_penalty": stockout_penalty
}
