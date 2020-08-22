from termcolor import cprint
'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

def play():
  exercise()

  numbers = []
  for i in range(0,5):
    number = int(input("Type a number: "))
    if (i == 0 or number > numbers[-1]): #se o i for o primeiro ou o valor de number for maior que o último termo da lista, coloque o número no final da lista.
      numbers.append(number)
      print(f"Adding in the end of the list...")
    else:
      position  = 0
      while (position < len(numbers)):
        if (number <= numbers[position]):
          numbers.insert(position, number)
          print(f"Adding in the position {position} od the list...")
          break  
        position +=1
  print("-="*30)
  print(f"The values typed were: {numbers}")        

def exercise():
  cprint("Create a program when the user can type five numerical values and registred them on a list, already in correct postion of insertion (don't use the sort()). At the end, show the list in ascedenting order on the screen.\n","green", attrs=["blink"])
