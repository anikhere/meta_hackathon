def _clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def grade_easy(result: dict) -> float:
    """Score = 1.0 - (stockouts / steps)"""
    steps = result.get('steps', 1)
    if steps <= 0:
        return 0.0
    stockouts = result.get('stockouts', 0)
    return _clamp(1.0 - stockouts / steps)


def grade_medium(result: dict) -> float:
    """Combined: 70% stockout penalty, 30% overstock penalty"""
    steps = result.get('steps', 1)
    if steps <= 0:
        return 0.0
    
    stockout_rate = result.get('stockouts', 0) / steps
    overstock_excess = result.get('excess_inventory', 0)
    overstock_rate = min(overstock_excess / (steps * 500), 1.0)
    
    score = 1.0 - (stockout_rate * 0.7 + overstock_rate * 0.3)
    return _clamp(score)


def grade_hard(result: dict) -> float:
    """Normalize profit: profit / 1000"""
    profit = result.get('profit', 0)
    return _clamp(profit / 1000.0)
