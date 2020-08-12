from termcolor import colored

'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

def play():
  exercise()

  salary = float(input(colored("Type the salary employee: R$", "yellow")))

  if (salary > 1250):
    print(f"This increases 10% is R${salary*0.10:.2f}, and total salary R${salary*1.10:.2f}")
  else:
    print(f"This increases 15% is R${salary*0.15:.2f}, and total salary R${salary*1.15:.2f}") 

def exercise():
  print(colored("Write a program that asks the salary of a employee and calculete the value of your increases. For salary bigger than R$1250.00, calculate a icreases of 10%. For the smaller or equal, the increases is of 15%. \n", "magenta"))
