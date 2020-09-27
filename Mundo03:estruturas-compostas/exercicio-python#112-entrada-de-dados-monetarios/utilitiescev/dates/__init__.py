def read_money(msg):
    valid = False

    while not valid:
        value = str(input("Enter the value: ")).replace(",", ".").strip()
        if value.isalpha() or value == "":
            print(f"\033[0;31mERROR: \"{value}\" is invalid.\033[m")
        else:
            valid = True
            return float(value)


