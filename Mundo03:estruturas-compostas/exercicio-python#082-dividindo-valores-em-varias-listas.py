from termcolor import cprint
'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

def play():
  exercise()

  numbers = []

  while(True):
    number = int(input("Type a number: "))
    numbers.append(number)
    to_continue = " "
    while(to_continue not in "YN"):
      to_continue = str(input("Do you want to continue? ")).upper().strip()
    if (to_continue == "N"):
      break
  
  even_numbers = []
  odd_numbers = []
  for i in range(len(numbers)):
    if (numbers[i] % 2 == 0):
      even_numbers.append(numbers[i])
    else:
      odd_numbers.append(numbers[i])

  print("-="*30)
  print(f"numbers = {numbers}")    
  print(f"even_numbers = {even_numbers}")
  print(f"odd_numbers = {odd_numbers}")
  

def exercise():
  cprint("Create a program that will reads several numbers and put on a list. After this, create two extra list that will contain only even values and the odd values entered, respective. At the end, show the content of the three generate list.\n","green", attrs=["blink"])
