from termcolor import cprint
'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
'''

def play():
  exercise()

  input_numbers = False
  numbers = []
  while(not input_numbers):
    number = int(input("Type a number: "))
    
    if (number not in numbers):
      numbers.append(number)
      print("Added value successfully...")
    else:
      print("This number already exist.") 
    to_continue = " "
    while(to_continue not in "YN"):
      to_continue = str(input("Do you want to continue? [Y/N] ")).upper().strip()

    if to_continue == "N":
      break
  
  print("-="*30)
  print("\nThe added numbers in ascending order were: ", end="")
  numbers.sort()
  for i, v in enumerate(numbers):
    print(f"{v}", end=" ") 


def exercise():
  cprint("Create a program where the user can type several numerical values and registred them on a list. If the number already exists inside, it will not be added. At the end, all the unique values ​​entered will be displayed, in ascending order. \n","green", attrs=["blink"])
