from termcolor import cprint
from time import sleep

'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

def play():
  exercise()

  end = False
  
  numbers = []
  for i in range(2):
    number = int(input(f"Type the {i+1}º number: "))
    numbers.append(number)

  while(not end):
    
    print("""\n[1] add
[2] multiply
[3] bigger
[4] new numbers
[5] exit the program""")
    
    option = int(input("Choice an option of above menu: "))
    
    if option == 1:
      add = sum(numbers)
      print(f"\nThe add of numbers {numbers[0]} and {numbers[1]} is {add}")
    elif option == 2:
      multiply = numbers[0] * numbers[1]
      print(f"\nThe multiplication of numbers {numbers[0]} and {numbers[1]} is {multiply}")
    elif option == 3:
      bigger = max(numbers)
      print(f"\nThe bigger of numbers between {numbers[0]} and {numbers[1]} is {bigger}")
    elif option == 4:
      print("\nType the new numbers...")
      numbers = []
      for i in range(2):
        number = int(input(f"Type the {i+1}º number: "))
        numbers.append(number)
      print(f"The new numbers are {numbers[0]} and {numbers[1]}")  
    elif option == 5:
      end = True    
    else:
      print("invalid Option... Try again!")
    print("=-="*10)
    sleep(2)
  print("Check Back Often!")





def exercise():
  cprint(f"""Create a program that reads two values ​​and shows a menu on the screen:
[1] add
[2] multiply
[3] bigger
[4] new numbers
[5] exit the program
Your program must perform a requested operation in each case..
   \n""","green", attrs=["blink"])

