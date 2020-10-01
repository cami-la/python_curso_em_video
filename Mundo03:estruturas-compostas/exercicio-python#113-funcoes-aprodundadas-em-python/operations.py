def read_integer(msg):
    while True:
        try:
            number = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mError, please type a integer valid number.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUser preferred to leave the field empty.\033[m")
            return 0
        else:
            return number


def read_real(msg):
    while True:
        try:
            number = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mError, please type a real valid number.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[031mUser preferred to leave the field empty.\033[m")
        else:
            return number
