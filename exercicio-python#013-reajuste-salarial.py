from termcolor import colored, cprint
'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

def play():
  exercise()

  salary = float(input("Type the salary: R$"))

  #aumento de 15% é: 1 + 0.15.
  print(f"The new salary with 15% up is R${salary*1.15:.2f}")

def exercise():
  cprint("Make a algorithm to read the salary of the a employee and show its new salary, with 15% up.\n","green", attrs=["blink"])
