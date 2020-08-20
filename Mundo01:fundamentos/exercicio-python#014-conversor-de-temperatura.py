from termcolor import colored, cprint
'''
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''

def play():
  exercise()

  c = float(input("Type the temperature in degree Celsius: "))
  f = ((9*c)/5) + 32

  print(f"This {c}℃  in Fahrenheit in {f:.1f}℉")

def exercise():
  cprint("Write a program to convert a temperature typing in degree Celsius and convert to degree Fahrenheit.\n","green", attrs=["blink"])
