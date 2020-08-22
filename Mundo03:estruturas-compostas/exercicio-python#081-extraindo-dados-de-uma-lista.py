from termcolor import cprint
'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

def play():
  exercise()

  numbers = []
  
  while(True):
    number = int(input("Type a number: "))
    numbers.append(number)
    
    to_continue = " "
    while (to_continue not in "NY"):
      to_continue = str(input("Do you want to continue? ")).upper().strip()
    if (to_continue == "N"):
      break
  print("=-"*40)
  print(f"{len(numbers)} numbers were entered")
  numbers.sort(reverse=True)
  print(f"{numbers}")
  if (5 in numbers):
    print("The number 5 was found in positions: ", end=" ")
    for index, value in enumerate(numbers):
      if value == 5:
        print(f"{index}", end=" ")
  else:
    print("The number 5 wasn't found on the list: ", end=" ")
  




def exercise():
  cprint("""Create a program that will read severel numbers and put on a list. After this, show:
A) How many numbers were typed
B) The list of values, ascending order
C) If the value 5 was typed and there is or there isn't on the list \n""","green", attrs=["blink"])
