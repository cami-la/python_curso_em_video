from termcolor import cprint
'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
def play():
  exercise()

  main_list = []
  odd_list = []
  even_list = []

  for i in range(3):
    number = int(input(f"Enter the {i+1}o. number of the list: "))
    if (number % 2 == 0):
      even_list.append(number)      
    else:
      odd_list.append(number)
      
  main_list.append(even_list[:])
  main_list.append(odd_list[:])  
     
  print("-="*30)
  print(f"Main List {main_list}")
  even_list.sort()
  print(f"List even in ascending order [{even_list}]")
  odd_list.sort()
  print(f"List odd in ascending order [{odd_list}]")
  
def exercise():
  cprint("Create a program where the user can enter seven numerical values ​​and register them in a single list that keeps the odd and even values ​​separate. At the end, show even and odd values ​​in ascending order.\n", "green", attrs=["blink"])
