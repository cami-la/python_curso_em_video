'''
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
'''

def play():
  exercise()

  # o comando input pede uma entrada e salva ela em uma variável
  name = input("Type your name: ")
  # "f" na frente da string seguido de {} é a abreviação de .format()
  print(f"Welcome, {name}!")


def exercise():
  print("Make a program to read the name person and show a menssage welcome.\n")
