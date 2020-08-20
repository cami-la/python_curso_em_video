from termcolor import colored, cprint
'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

def play():
  exercise()

  number = int(input("Type a number that will converted: "))
  print("""Choice a of bases to convertion:
  [1] binary
  [2] octal
  [3] hexadecimal\n""")
  option = int(input("Your choice is: "))

  if (option == 1):
    print(f"{number} converted in binary is {bin(number)[2:]}")
  elif(option == 2):
    print(f"{number} converted in octal is {oct(number)[2:]}")
  elif(option == 3):
    print(f"{number} converted in hexadecimal is {hex(number)[2:]}")
  else:
    print("Invalid number!")
    

def exercise():
  cprint("Write a program in Python than reads a integer any number and ask to a user choice what would the base of covertion: 1 to binary - 2 to octal - 3 hexadecimal.\n","green", attrs=["blink"])
