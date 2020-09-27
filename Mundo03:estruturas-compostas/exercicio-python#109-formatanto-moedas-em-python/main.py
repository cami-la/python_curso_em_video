from termcolor import cprint
from list_of_exercises.exercise109 import operations

def play():
  price = float(input("Enter the price: R$" ))

  print(f"The half of {operations.format_currency(price)} is {operations.half(price, True)}")
  print(f"The double of {operations.format_currency(price)} is {operations.double(price, True)}")
  print(f"Increasing 10% have {operations.increase(price, 10, True)}")
  print(f"Decreasing 13% have {operations.decrease(price, 13, True)}")

def exercise():
  cprint("Modify the functions that were created in challenge 107 so that they accept one more parameter, informing whether or not the value returned by them will be formatted by the currency () function, developed in challenge 108.\n", "green", attrs=["blink"])
