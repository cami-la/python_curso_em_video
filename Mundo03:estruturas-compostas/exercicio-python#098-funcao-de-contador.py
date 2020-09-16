from termcolor import cprint
from time import sleep
"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

def play():
  exercise()
  counter(1, 10, 1)
  print()
  counter(10, 0, 2)
  print()

  first_number = int(input("First Number: ")) 
  last_number = int(input("Last Number: "))
  step_number = int(input("Step Number: "))
  counter(first_number, last_number, step_number)

def exercise():
  cprint("""Make a program that has a function called counter (), that receives three parameters: start, end and step. Your program has to perform three counts using the function created:
a) from 1 to 10, from 1 to 1
b) 10 to 0, 2 in 2
c) a personalized count\n""","green", attrs=["blink"])

def counter(start, stop, step):
  print("-="*20)

  if step < 0:
    step *= -1
  if step == 0:
    step = 1   

  print(f"Count from {start} to {stop} of {step} in {step}: ")
  
  if start < stop:
    count = start
    while(count <= stop):
      print(count, end=" ", flush=True)
      sleep(0.5)
      count += step
    print("END!") 
  else:
    count = start
    while(count >= stop):
      print(count, end=" ", flush=True)
      sleep(0.5)
      count -= step
    print("END!")   
  print("-="*20)
  
