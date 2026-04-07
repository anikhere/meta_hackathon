class Observation:
    def __init__(self, inventory: int, demand: int):
        self.inventory = inventory
        self.demand = demand

    def to_dict(self):
        return {
            "inventory": self.inventory,
            "demand": self.demand
        }
    