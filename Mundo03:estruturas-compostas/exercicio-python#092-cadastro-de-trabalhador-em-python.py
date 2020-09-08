from termcolor import cprint
from datetime import date

'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

def play():
  exercise()

  employee = {}

  employee["name"] = str(input("name: "))
  employee["year of birth"] = int(input("year of birth: "))
  employee["age"] = date.today().year - employee["year of birth"]
  employee["CTPS"] = int(input("CTPS: "))
  
  if employee["CTPS"] != 0:
    employee["contract_year"] = int(input("year Contract: "))
    employee["salary"] = float(input("salary: R$"))
    employee["retirement"] = employee["age"] + ((employee["contract_year"] + 35) - date.today().year)
  
  print("=-" *30)

  for k, v in employee.items():
    print(f"{k} has the value {v}.")



def exercise():
  cprint("Create a program that reads your name, year of birth and work permit and records it (aged) in a dictionary. If the CTPS happens to be different from ZERO, the dictionary will also receive the year of hire and the salary. Calculate and add, in addition to age, how old the person will retire.\n","green", attrs=["blink"])
