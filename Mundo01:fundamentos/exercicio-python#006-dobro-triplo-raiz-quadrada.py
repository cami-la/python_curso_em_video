from termcolor import colored, cprint
'''
Crie um algorítmo que leia um número e mostre o seu dobro, o seu triplo e a raiz quadrada.
'''

def play():
  exercise()

  number = int(input("Type a number: "))

  #:.2f significa que é para formatar o resultado e pegar apenas 2 casa decimais.
  # a raiz quadrada também pode ser calculada pela potência pow(number,(1/2)) ou pow(number,0.5)
  print(f"The {number} has: double = {number * 2}, triple = { number * 3} and root = {number ** 0.5:.2f}.")

def exercise():
  cprint("Crie um algorítmo que leia um número e mostre o seu dobro, o seu triplo e a raiz quadrada.","green", attrs=["blink"])
