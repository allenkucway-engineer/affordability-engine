def extract_income(user):

    if user is None:
        raise ValueError('user is required')
    if not isinstance(user, dict):
        raise TypeError('user must be a dict')
    if 'income' not in user:
        raise ValueError('user["income"] is required')
    income = user['income']
    if income is None:
        raise ValueError('user["income"] cannot be None')
    
    return income    
