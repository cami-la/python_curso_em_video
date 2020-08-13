from termcolor import colored, cprint
'''
Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 
Considere US$ = R$3.27
'''

def play():
  exercise()

  converter = 3.27
  money = float(input("How much money do you have? R$"))

  print(f"Money R${money} - Money US${money/converter:.2f}")

def exercise():
  cprint("Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.\n","green", attrs=["blink"])  
