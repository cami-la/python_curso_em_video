from termcolor import colored, cprint
'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

def play():
  exercise()

  value_house = float(input("How much cost the house? R$ "))
  salary_byer = float(input("How much the salary of employee? R$ "))
  how_old = float(input("How old do you want to pay the house? "))

  installment = value_house / (how_old*12)

  if (installment > salary_byer*0.3):
    print("\nYour ask of loan was denied.")
  else:
    print(f"\nYour ask of loan was approved in {how_old} x R${installment:.2f}.")  

def exercise():
  cprint("Write a program to approv the bank loan to the buy of a house. Ask the value of the house, the salary of buyer and in how old will he pay. If the monthly installment exceed 30% of the salary, the loan will be denied.\n","green", attrs=["blink"])  
