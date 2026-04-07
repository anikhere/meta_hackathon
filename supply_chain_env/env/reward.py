from pydantic import BaseModel, Field


class RewardInfo(BaseModel):
    profit: float = Field(..., description="Revenue from sales")
    holding_penalty: float = Field(..., description="Holding cost")
    stockout_penalty: float = Field(..., description="Stockout penalty")
    total_reward: float = Field(..., description="Net reward")


def compute_reward(sold: int, demand: int, inventory: int, price: int = 10) -> tuple[float, dict]:
    profit = sold * price
    holding_penalty = inventory * 0.1
    stockout_penalty = max(0, demand - sold) * 5
    total_reward = profit - holding_penalty - stockout_penalty
    
    return total_reward, {
        "profit": profit,
        "holding_penalty": holding_penalty,
        "stockout_penalty": stockout_penalty,
        "total_reward": total_reward,
    }
