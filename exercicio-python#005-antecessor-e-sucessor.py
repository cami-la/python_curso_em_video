'''
Faça um programa que leia um número inteiro e mostre na tela o seu antecessor e seu sucessor.
'''

def play():
  exercise()

  number = int(input("Type a number: "))

  #o antecessor de um número é ele -1 e o sucessor é +1
  print(f"The predecessor of the {number} is {number - 1} and the successor is {number + 1}")


def exercise():
  print("Make a program to read a integer number and show on the screen its predecessor and its successor.\n")
