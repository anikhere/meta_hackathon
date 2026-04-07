# SupplyChainEnv

A minimal OpenEnv-compliant supply chain inventory management simulation.

## Problem
Manage inventory and demand over a fixed horizon with two ordering actions: `order_small` and `order_large`.

## Environment
- `SupplyChainEnv` exposes `reset()` and `step(action)`.
- Episodes run for 30 steps.
- The state includes `inventory`, `money`, and `demand`.

## Action space
- `order_small`: add a small restock
- `order_large`: add a larger restock

## Observation space
- `inventory`: current inventory level after sales
- `demand`: demand for the current step

## Reward
- Reward is profit from sales minus holding costs and stockout penalties.

## How to run
From the `supply_chain_env` directory:

```bash
python scripts/run_baseline.py
```
