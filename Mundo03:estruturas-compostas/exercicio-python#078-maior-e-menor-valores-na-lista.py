from termcolor import cprint
'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
'''

def play():
  exercise()
  #o valor do maior e menor número é 0 pois ainda não existe.
  highest = lowest = 0
  numbers = []

  for i in range(5):
    number = int(input(f"Type the value to position {i}: "))
    numbers.append(number)
    if i == 0: #quando começar o laço (primeira posição i = 0, o valor da primeira posição é o maior e o menor número ao mesmo tempo, pois só tem ele.)
      highest = lowest = numbers[i]
    else:
      if (numbers[i] > highest):
        highest = numbers[i]
      if (numbers[i] < lowest):
        lowest = numbers[i]


  print("=-"*30)  
  print(f"You typed the values {numbers}.")
  
  print(f"The highest value typed was {highest} in positions ", end="")
  for index, value in enumerate(numbers):
    if (value == highest):
      print(f"{index}...", end="")
  print("")
  
  print(f"The lowest value typed was {lowest} in positions ", end="")
  for index, value in enumerate(numbers):
    if (value == lowest):
      print(f"{index}...", end="")
  
  
def exercise():
  cprint("Make a program to reads 5 numerical values and save them on the list. At the end, show what was the largest and the smallest value typed and the its respective positions.\n","green", attrs=["blink"])
