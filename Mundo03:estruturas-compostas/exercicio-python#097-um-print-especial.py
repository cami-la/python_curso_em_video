from termcolor import cprint
'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''

def play():
  exercise()

  message = str(input("Type a message: "))

  specialprint(message)

def exercise():
  cprint("Make a program that has a function called write (), which takes any text as a parameter and displays a message with an adaptable length.\n","green", attrs=["blink"])

def specialprint(msg):
  length = len(msg)+2
  print("~"*length)
  print(f" {msg}  ")
  print("~"*length)
  
