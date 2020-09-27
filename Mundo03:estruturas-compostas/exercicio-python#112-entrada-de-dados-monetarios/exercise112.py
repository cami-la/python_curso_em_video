from termcolor import cprint
from list_of_exercises.exercise112.utilitiescev import dates, operations

def play():
  exercise()
  price = dates.read_money("Enter the value: R$")

  operations.resume(price, 35, 22)

def exercise():
  cprint("Within the utilidadesCeV package that we created in challenge 111, we have a module called data. Create a function called readMoney () that is able to function as the imputed function (), but with data validation to accept only values ​​that are monetary.\n", "green", attrs=["blink"])
