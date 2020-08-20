from termcolor import cprint
'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

def play():
  exercise()

  value = int(input("type the value: R$"))

  bill_50 = value // 50
  value %= 50
  print(value)
  bill_20 = value // 20
  value %= 20
  print(value)
  bill_10 =  value // 10
  value %= 10
  print(value)
  bill_1 =  value // 1
  print(value)
  
  if (bill_50 != 0):
    print(f"Total of {bill_50} bill of R$50")
  if (bill_20 != 0):
    print(f"Total of {bill_20} bill of R$20")  
  if (bill_10 != 0):
    print(f"Total of {bill_10} bill of R$10")
  if (bill_10 != 0):  
    print(f"Total of {bill_1} bill of R$1")

def exercise():
  cprint("Creat a program that simulates the functioning of the ATM. At the beginning, ask to user what will be the amout will be withdraw (integer number) and the program will inform how many bill of each value will be delivered. (Consider that the cash has bill f R$50, R$20, R$10 and R$1.)\n","green", attrs=["blink"])


  
