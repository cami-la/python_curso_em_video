from math import trunc
'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''

def play():
  exercise()

  real_number = float(input("Type a real number: "))

  #várias formas de mostrar o número
  print(f"The whole portion of number {real_number} is {real_number:.0f}") #neste caso, arredonda para o maior
  print(f"The whole portion of number {real_number} is {int(real_number)}")
  print(f"The whole portion of number {real_number} is {trunc(real_number)}")


def exercise():
  print("Create a program to read a any real number by keyboard and show on the screen the its whole portion.\n")
