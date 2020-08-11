'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
'''

def play():
  exercise()

  number = int(input("\nType a number between 0 and 9999: "))  
  
  unity = number // 1 % 10 
  ten = number // 10 % 10
  hundred = number  // 100 % 10
  thousands = number // 1000 % 10
  
  print(f"Analyzing the number {number}...")

  print(f"Unity {unity}")
  print(f"ten {ten}")
  print(f"hundred {hundred}")
  print(f"thousands {thousands}")


def exercise():
  print("Make a program to read a number between 0 and 9999 and show on the screen each digit separated.\n")  
