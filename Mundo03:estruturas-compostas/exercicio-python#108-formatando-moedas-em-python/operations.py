def half(value=0):
    return value / 2


def double(value=0):
    return value * 2


def increase(value=0, tax=0):
    return value * (tax / 100 + 1)


def decrease(value=0, tax=0):
    return value * (1 - tax / 100)


def format_currency(value=0, symbol="R$"):
    return f"{symbol}{value:>.2f}".replace(".", ",")

