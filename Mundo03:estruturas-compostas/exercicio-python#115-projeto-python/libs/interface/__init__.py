from list_of_exercises.exercise113.operations import read_integer

def line(length=42):
    return "-" * length

def header(txt, length=42):
    print(line())
    print(txt.center(length))
    print(line())

def menu(param):
    header("MAIN MENU")
    count = 1
    for i in param:
        print(f"\033[33m{count}\033[m - \033[34m{i}\033[m")
        count += 1
    print(line())

    option = read_integer("\033[32mYour Option: \033[m")
    return option

