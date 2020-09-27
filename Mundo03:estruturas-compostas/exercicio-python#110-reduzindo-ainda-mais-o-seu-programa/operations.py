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
    res = value * (1 - (tax / 100))
    return res if not formated else format_currency(res)


def format_currency(value=0, symbol="R$"):
    return f"{symbol}{value:>.2f}".replace(".", ",")


def resume(value, tax_incre=10, tax_decre=5):
    print("-"*30)
    print("RESUME OF VALUE".center(30))
    print("-"*30)

    print(f"Analyzed price \t{format_currency(value)}")
    print(f"Double of price \t{double(value, True)}")
    print(f"Half of price \t{half(value, True)}")
    print(f"{tax_incre}% of increment \t{increase(value, tax_incre, True)}")
    print(f"{tax_decre}% of increment \t{decrease(value, tax_decre, True)}")
    print("-"*30)


