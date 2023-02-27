
def add(x, y):
    """Add Function"""
    return x + y


def substract(x, y):
    """Substract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divid Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y