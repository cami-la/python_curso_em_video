from termcolor import cprint
from list_of_exercises.exercise108 import operations

def play():
  exercise()
  price = float(input("Enter the price: R$" ).replace(",", "."))

  print(f"The half of {operations.format_currency(price)} is {operations.format_currency(operations.half(price))}")
  print(f"The double of {operations.format_currency(price)} is {operations.format_currency(operations.double(price))}")
  print(f"Increasing 10% have {operations.format_currency(operations.increase(price, 10))}")

def exercise():
  cprint("Adapte challenge code # 107, creating an additional function called currency () that can show the numbers as a formatted monetary value.\n", "green", attrs=["blink"])
