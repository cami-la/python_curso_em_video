from termcolor import colored, cprint
'''
Escreva um programa que leia dois números inteiros, compare-os and mostre na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

def play():
  exercise()

  numbers = []
  for i in range(2):
    number = int(input(f"Type the {i+1}º number: "))
    numbers.append(number)

  if (numbers[0] > numbers[1]):
    print(f"The first number {max(numbers)} is the greater.")
  elif (numbers[0] < numbers[1]):
    print(f"The second number {max(numbers)} is the greaster")
  else:
    print(f"There first number {numbers[0]} and second number {numbers[1]} is equal. There is no great.")      

def exercise():
  cprint("""Write a program that reads two integers numbers, comparing them and show on the screen a menssage:
  - The first number is greater;
  - The second number is greater;
  - There is no greater value, the two are equal.\n""","green", attrs=["blink"])
