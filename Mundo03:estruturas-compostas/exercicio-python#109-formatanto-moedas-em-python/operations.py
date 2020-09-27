def half(value=0, formated=False):
    res = value / 2
    return res if not formated else format_currency(res)


def double(value=0, formated=False):
    res = value * 2
    return res if not formated else format_currency(res)


def increase(value=0, tax=0, formated=False):
    res = value * (tax / 100 + 1)
    return res if not formated else format_currency(res)


def decrease(value=0, tax=0, formated=False):
    res = value * (1 - tax / 100)
    return res if not formated else format_currency(res)


def format_currency(value=0, symbol="R$"):
    return f"{symbol}{value:>.2f}".replace(".", ",")

