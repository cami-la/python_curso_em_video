from termcolor import cprint
'''
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''

def play():
  exercise()

  matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  for line in range(3):
    for column in range(3):
      matrix[line][column] = int(input(f"Enter the [{line}, {column}] number: "))
  
  print(matrix)
  print("-="*30)
  for line in range(3):
    for column in range(3):
      print(f"[{matrix[line][column]:^5}]", end=" ")
    print() 


def exercise():
  cprint("Create a program that declares a 3x3 dimension matrix and fills in values ​​read from the keyboard. At the end, show the matrix on the screen, with the correct formatting.\n", "green", attrs=["blink"])
