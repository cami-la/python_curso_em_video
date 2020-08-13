from termcolor import colored, cprint
'''
Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
'''

def play():
  exercise()

  number = int(input("Type a number to show its mutiplication: "))
  print("\n")
  print("-" * 12)
  
  #o range percorre todo o intervalo de 0 a 10, o número 11 é apenas de referência, sempre será um a menos.
  for i in range(0,11):
    #para formatar, usa :2 para dar um espaço e simular 2 dígitos
    print(f"{number} x {i:2} = {number * i:2}")

  print("-" * 12)

def exercise():
  cprint("Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.\n","green", attrs=["blink"])
