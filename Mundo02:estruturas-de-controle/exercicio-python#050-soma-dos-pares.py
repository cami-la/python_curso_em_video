from termcolor import cprint
'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

def play():
  exercise()

  even_numbers = []
  for i in range(6):
    number = int(input(f"Type the {i+1}º number: "))

    if (number % 2 == 0):    
      even_numbers.append(number)
  
  print(even_numbers)

  print(f"The sum of {len(even_numbers)} even numbers typed is {sum(even_numbers)}")  
    
      

def exercise():
  cprint("Develop a program that reads six integers numbers and shows the sum of only those that are even. If the value entered is odd, ignore it.\n","green", attrs=["blink"])
