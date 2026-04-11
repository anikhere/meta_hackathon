import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'supply_chain_env'))

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from env.environment import SupplyChainEnv

app = FastAPI()
env = SupplyChainEnv()

class ResetRequest(BaseModel):
    task_name: Optional[str] = "easy"
    seed: Optional[int] = 42

class StepRequest(BaseModel):
    action: Optional[str] = "order_small"

@app.post("/reset")
def reset(req: ResetRequest = None):
    state = env.reset()
    return {
        "observation": {"inventory": state.inventory, "demand": state.demand},
        "done": False,
        "info": {}
    }

@app.post("/step")
def step(req: StepRequest):
    observation, reward, done, info = env.step(req.action)
    return {
        "observation": observation,
        "reward": {"total": float(reward)},
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    s = env.state()
    return {
        "episode_history": [],
        "inventory": s.inventory,
        "money": s.money,
        "demand": s.demand
    }

@app.get("/")
def root():
    return {"status": "ok", "env": "supply-chain-env"}
