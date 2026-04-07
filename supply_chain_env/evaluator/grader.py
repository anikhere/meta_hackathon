def _clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def grade_easy(result: dict) -> float:
    steps = result.get('steps', 0)
    if steps <= 0:
        return 0.0
    stockouts = result.get('stockouts', 0)
    return _clamp(1.0 - stockouts / steps)


def grade_medium(result: dict) -> float:
    steps = result.get('steps', 0)
    if steps <= 0:
        return 0.0
    stockout_rate = result.get('stockouts', 0) / steps
    overstock_rate = min(result.get('excess_inventory', 0) / (steps * 500), 1.0)
    score = 1.0 - (stockout_rate * 0.7 + overstock_rate * 0.3)
    return _clamp(score)


def grade_hard(result: dict) -> float:
    final_money = result.get('final_money', 0)
    profit = final_money - 10000
    return _clamp(profit / 1000.0)
