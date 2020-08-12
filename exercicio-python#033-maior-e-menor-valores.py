from termcolor import colored
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
  
  print(colored(f"The bigger number is {numbers_in_order[len(numbers_in_order)-1]}", "cyan"))
  print(colored(f"The smaller number is {numbers_in_order[0]}", "cyan"))

  print(min(numbers), max(numbers))


def exercise(): 
  print(colored("Make a program that reads three numbers and show wich is the bigger and wich is the smaller.\n", "magenta"))
