from termcolor import cprint
'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

def play():
  exercise()
  numbers = (int(input("Type a number: ")), 
  int(input("Type a number: ")), int(input("Type a number: ")), int(input("Type a number: ")))

  print(f"\nThe number 9 came up {numbers.count(9)} times")
  
  if 3 in numbers:
    print(f"The number 3 was in {numbers.index(3)+1}º position")
  else:
    print("There aren't number 3.")
  
  even_numbers = []
  for number in numbers:
    if number % 2 == 0:
      even_numbers.append(number)
  
  print("The even nummber typed were ", end="")
  for number in even_numbers:
    print(number, end=" ")   
  

  

  

def exercise():
  cprint("""Develop a program that reads four values by keyboard and save them on one tuple. At the end, show:
A) How often does the value 9 appear
B) In what positon was typed the first value 3
C) What were the even numbers\n""","green", attrs=["blink"])
