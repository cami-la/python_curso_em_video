'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

def play():
  exercise()

  number = int(input("Type an integer number: "))

  multiples = []
  for i in range(1, number+1):
    if (number % i == 0):
      multiples.append(i)        
    print(f"{i}", end=" ")  
  if (len(multiples) == 2):
    print(f"\n\033[31mThis number {number} is prime!\033[m")
  else:
    print(f"This number {number} isn't prime!")

  print(f"The number {number} was divisible {len(multiples)} times: {multiples}")     
       

def exercise():
  print("\n\033[32mMake a program to reads an integer number and says if it is or isn't an prime number.\n\033[m")
