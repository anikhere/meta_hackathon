# SupplyChainEnv - OpenEnv Compliant

A production-grade supply chain inventory optimization environment.

## Overview

Manage inventory and demand over a 30-step horizon. Decide when to order small amounts, large amounts, or do nothing.

## Environment

- **State**: inventory, money, demand
- **Actions**: order_small, order_large, do_nothing
- **Observations**: inventory, demand
- **Reward**: profit - holding_cost - stockout_penalty

## Tasks

1. **Easy**: Minimize stockouts
2. **Medium**: Balance inventory (reduce stockouts and overstock)
3. **Hard**: Maximize total profit

## Installation

```bash
pip install -r requirements.txt
```

## Running

### Baseline Inference
```bash
python inference.py
```

### Docker
```bash
docker build -t supply-chain-env .
docker run supply-chain-env
```

## OpenEnv Compliance

- Pydantic models for Observation, Action, Reward
- Standard step(action) → (observation, reward, done, info)
- reset() → observation
- state() → full internal state
- Valid openenv.yaml specification

## Project Structure

```
supply_chain_env/
  env/
    environment.py
    observation.py
    action.py
    reward.py
  tasks/
    easy.py
    medium.py
    hard.py
  evaluator/
    grader.py
  agents/
    (agent implementations)
  config/
    openenv.yaml
inference.py
requirements.txt
Dockerfile
```
