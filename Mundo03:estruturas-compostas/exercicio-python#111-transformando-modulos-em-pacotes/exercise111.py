from termcolor import cprint
from list_of_exercises.exercise111.utilitiescev import dates, operations

def play():
  exercise()
  price = float(input("Enter the price: R$" ))

  operations.resume(price, 35, 22)

def exercise():
  cprint("Create a package called utilidadesCeV that has two internal modules called currency and data. Transfer all the functions used in challenges 107, 108 and 109 to the first package and keep everything running.\n", "green", attrs=["blink"])
