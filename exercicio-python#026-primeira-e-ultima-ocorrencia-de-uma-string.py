from termcolor import colored, cprint
'''
Faça um programa que leia uma frase pelo teclado: 
- mostre quantas vezes aparece a letra "A",
- em que posição ela aparece a primeira vez 
- e em que posição ela aparece a última vez.
'''

def play():
  exercise() 

  phrase = str(input("Type a phrase: ").upper().strip())
  print(f"The letter 'A' come up {phrase.count('A')} times.")
  print(f"The letter 'A' come up by first time in {phrase.find('A')+1} position.")
  #aqui usa o rfind() para encontra a primeira posição começando da direita para a esquerda.
  print(f"The letter 'A' come up by last time in {phrase.rfind('A')+1} position.")

def exercise():
  cprint(""""Make a program to read a phrase by keyboard:
  - show how many times come up the letter 'A',
  - wich position it come up the first time,
  - and in wich position it come up the last time.\n""","green", attrs=["blink"])
