from termcolor import cprint
'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

def play():
  exercise()

  temporary_list = []
  main_list = []
  
  biggest = smallest = 0

  while(True):
    temporary_list.append(str(input("Enter the name's person: ")).capitalize().strip());
    temporary_list.append(float(input("Enter the weight's person: ")))
    if (len(main_list) == 0):
        biggest = smallest = temporary_list[1]
    else:
      if (temporary_list[1] > biggest):
          biggest = temporary_list[1]
      if (temporary_list[1] < smallest):
          smallest = temporary_list[1]    
    main_list.append(temporary_list[:])
    temporary_list.clear()

    to_continue = " "  
    while(to_continue not in "YN"):
      to_continue = str(input("Do you want to contine? [Y/N] ")).upper().strip()
    if (to_continue == "N"):
      break 


  print("-="*30)
  print(f"Were registred {len(main_list)} people.")
  print(f"The biggest weight was {biggest}kg", end=" ")
  for i in main_list:
    if (i[1] == biggest):
      print(f"{[i[0]}]", end=" ")
  print(f"\nThe smallest weight was {smallest}kg", end=" ")
  for i in main_list:
    if (i[1] == smallest):
      print(f"[{i[0]}]", end=" ")

def exercise():
  cprint("""Make a program that reads the name and weight of severeal people, salving all in the list. At the end, shows: 
A) How many peoples were resgistred
B) A list with heavier people
B) A list with lighter people\n""","green", attrs=["blink"])
