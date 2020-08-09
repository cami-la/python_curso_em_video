'''
Crie um programa que leia dois numeros e mostre a soma entre eles.
'''

def play():
  exercise()
  
  #aqui, na frente do input, foi preciso colocar o int para dizer que o input será um número inteiro e não uma string.
  number1 = int(input("Type the first number: "))
  number2 = int(input("Type the second number: "))

  print(f"\nThe sum between {number1} + {number2} is {number1 + number2}")


  ''''
  numbers = [number1, number2] Você pode criar um array, tuple, e usar o sum()
  
  print(f"The sum between {number1} + {number2} is {sum(numbers)}")
  '''  
  

def exercise():
  print("Create a program to read two numbers and show the sum between them.\n")
