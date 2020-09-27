from termcolor import cprint
from list_of_exercises.exercise107 import operations

def play():
  exercise()

  price = float(input("Enter the price: R$" ))

  print(f"The half of {price} is {operations.half(price)}")
  print(f"The double of {price} is {operations.double(price)}")
  print(f"Increasing 10% have {operations.increase(price, 10)}")

def exercise():
  cprint("Create a module called coin.py that has the built-in functions increase (), decrease (), double () and half (). Also make a program that imports this module and uses some of these functions.\n", "green", attrs=["blink"])
