from termcolor import colored, cprint
'''
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''

def play():
  exercise()

  for i in range(0, 51, 2):
    print(i, end= " ")

def exercise():
  cprint("Create a program that show on the screen all even numbers that are in the range between 1 and 50.\n","green", attrs=["blink"])
