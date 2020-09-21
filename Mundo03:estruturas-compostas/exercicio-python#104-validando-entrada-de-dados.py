from termcolor import cprint
'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''

def play():
  exercise()

  number = read_int("Type a number: ")
  print(f"You just entered the number {number}")


def exercise():
  cprint("Create a program that has the function readInt (), which will work similarly to the input () function of Python, only doing the validation to accept only a numeric value. Ex: n = LeiaInt ('Type an n:')\n","green", attrs=["blink"])

def read_int(mensage):

  ok = False
  value = 0

  while(not ok):
    n = str(input(mensage))
    if n.isnumeric():
      value = int(n)
      ok = True
      return value
    else:
      cprint("ERROR. Type a integer number valid!", "red")  
