from termcolor import cprint
'''
Mostre a tabuada de um número que o usuário escolher.
'''

def play():
  exercise()

  multiplication = int(input("Choice a number to multiplication: "))

  for i in range(0,11):
    print(f"{multiplication} x {i:2} = {multiplication * i:2}")


def exercise():
  cprint("Show the multiplication of a number that the user chooses.\n","green", attrs=["blink"])
