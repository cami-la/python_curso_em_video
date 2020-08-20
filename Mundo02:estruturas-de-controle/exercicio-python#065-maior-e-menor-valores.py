from termcolor import cprint
'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

def play():
  exercise()

  numbers = []
  stop = False

  while (not stop):
    number = int(input("Type a number: "))
    numbers.append(number)
    
    ask = str(input("Do you want to continue? [Y/N] ")).upper().strip()
    if ask == "N":
      break 

  print(f"The avarege values is {sum(numbers)/len(numbers)}, the bigger value was {max(numbers)} and the smaller value is {min(numbers)}.")

def exercise():
  cprint("Create a program to reads several values by keyboard. At the end of run, show the averege between every the values and which was the bigger and the smaller values have been read. The program must ask to user if he wants or don't wants to continue the typing values.","green", attrs=["blink"])

