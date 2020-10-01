'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''
from termcolor import cprint
from list_of_exercises.exercise113.operations import read_integer, read_real

def play():
  exercise()
  integer_number = read_integer("Enter a integer number: ")
  real_number = read_real("Enter a real number: ")

  print(f"The integer number was {integer_number} and the real number was {real_number}.")

def exercise():
  cprint("Rewrite the readInt () function that we did in challenge 104, now including the possibility of entering an invalid type number. Take advantage and also create a function readFloat () with the same functionality.\n", "green", attrs=["blink"])
