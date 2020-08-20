from termcolor import cprint
from random import randint
from time import sleep
'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

def play():
  exercise()

  numbers = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
  
  print(f"The generate numbers are: {numbers}")
  print(f"The smallest number is {min(numbers)} and largest {max(numbers)}")

def exercise():
  cprint("Create a program that will generate five random numbers and put on a tuple. After this, show the list of the generate numbers and also indicate the smallest and the largest value that are in the tuple.\n","green", attrs=["blink"])  
