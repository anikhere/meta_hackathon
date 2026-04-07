from env.entity import State
import numpy as np 
import random
from env.reward import compute_reward
from env.observation import Observation


class SupplyChainEnv:
    def __init__(self):
        self._state = None
        self.current_step = 0
        self.max_steps = 30
    
    def reset(self):
        self._state = State(
            inventory=1500,
            money=10000,
            demand=random.randint(5,20)
        )
        self.current_step = 0
        return self._state
    
    def step(self, action):
        state = self._state
        if action == 'order_small':
            state.inventory += 50
        elif action == 'order_large':
            state.inventory += 150
        elif action == 'do_nothing':
            pass
        
        demand = random.randint(5, 20)
        sold = min(state.inventory, demand)
        state.inventory -= sold
        state.money += sold * 10
        state.demand = demand
        
        obs_obj = Observation(inventory=state.inventory, demand=state.demand)
        observation = obs_obj.to_dict()
        
        reward, reward_info = compute_reward(
            sold=sold,
            demand=demand,
            inventory=state.inventory,
        )
        
        self.current_step += 1
        done = self.current_step >= self.max_steps
        info = {
            'sold': sold,
            'demand': demand
        }
        return observation, reward, done, info
    
    def state(self):
        return self._state
