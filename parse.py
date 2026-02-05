def parse_income(value):
    try:
        income = float(value)
    except (TypeError, ValueError):
        raise ValueError(f'income must be numeric, got: {value!r}')
    
    return income
