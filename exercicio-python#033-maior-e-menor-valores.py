from termcolor import colored, cprint
'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

def play():
  exercise()

  numbers = []
  
  for i in range(3):
    number = int(input(f"Type the {i+1}º number: "))
    numbers.append(number)
  
  numbers_in_order = sorted(numbers) 
  
  print(colored(f"The bigger number is {numbers_in_order[len(numbers_in_order)-1]}"))
  print(colored(f"The smaller number is {numbers_in_order[0]}"))

  print(min(numbers), max(numbers))


def exercise(): 
  cprint(colored("Make a program that reads three numbers and show wich is the bigger and wich is the smaller.\n" ,"green", attrs=["blink"]))
