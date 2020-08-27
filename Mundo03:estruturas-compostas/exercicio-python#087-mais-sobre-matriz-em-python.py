from termcolor import cprint
'''Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

def play():
  exercise()

  matrix = [[], [], []]
  sum_values = sum_value_thirth_column = second_row_largest = 0

  #cada par de conchete dentro da matriz representa uma linha
  for line in range(3):
    #cada item dentro da linha representa uma coluna
    for column in range(3):
      matrix[line].append(int(input(f"Enter a number of [{line}, {column}] in matrix: ")))    
  print("=-"*30)
  for line in range(3):
    for column in range(3):
      sum_values += matrix[line][column]
      print(f"[{matrix[line][column]:^5}]", end = " ") 
    print()   
  print("=-"*30)
  print(f"This sum is {sum_values}")
  for line in range(3):
    sum_value_thirth_column += matrix[line][2]
  print(f"The sum of thirth column {sum_value_thirth_column}")
  
  for column in range(3):
    if (column == 0):
      second_row_largest = matrix[1][0]
    elif (matrix[1][column] > second_row_largest):
      second_row_largest = matrix[1][column]
  print(f"This largest of second line is: {second_row_largest}")    

def exercise():
  cprint("""Create a program that declares a 3x3 dimension matrix and fills in values ​​read from the keyboard. At the end, show the matrix on the screen, with the correct formatting: 
A) The sum of all the even values ​​entered.
B) The sum of the values ​​in the third column.
C) The highest value of the second line.\n""", "green", attrs=["blink"])

