from termcolor import cprint
'''
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
'''

def play():
  exercise()

  print("-"*30)
  print("Fibonacci Sequence")
  print("-"*30)
  
  number = int(input("How much terms do you want to show? "))
  
  last_term = 0
  penultimate_term = 1
  
  print("~"*30)
  
  if ((number == 1) or (number == 2)):
    print("1")
  else:
    print(f"{last_term} ⇢ ", end=" ")
    for i in range(1, number):
      actual_term = last_term + penultimate_term
      penultimate_term = last_term
      last_term = actual_term
      print(f"{last_term}", end=" ⇢ ")
  print("end")  
    

def exercise():
  cprint("""Write the program to reads a any integer N and show on the screen the N first elements of a Fibonacci sequence.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8\n""","green", attrs=["blink"])


