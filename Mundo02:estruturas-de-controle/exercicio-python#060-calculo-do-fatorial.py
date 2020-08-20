from termcolor import cprint
from math import factorial
'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
def play():
  exercise()

  number = int(input("Type a number and find out its factorial: "))
  
  result = factorial(number)
  print(f"The factorial of number {number}! is {result}")

  ''''
  factorial = 1
  print(f"{number}! =", end= " ")
  for i in range(number, 0, -1):
    factorial *= i 
    print(f"{i}", end=" ")
    print("x" if i != 1 else "=", end=" ")
  print(f"{factorial}")  
  '''
  '''
  count = number
  factorial = 1
  print(f"{number}! = ", end= " ")
  while (count > 0):
      factorial *= count    
      
      print(f"{count}", end=" ")
      print("x" if count != 1 else "=", end=" ")
      count -= 1
  print(f"{factorial}")    
  '''

def exercise():
  cprint("""Make a program to reads any number and show the its factorial.
  Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120\n""","green", attrs=["blink"])

