from random import randint 
from time import sleep
from termcolor import cprint
'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

def play():
  exercise()

  numbers = []
  draw(numbers)
  some(numbers)

def exercise():
  cprint("Create a program that has a function called vote () that will take a person's year of birth as a parameter, returning a literal value indicating whether a person has a DENIED, OPTIONAL and MANDATORY vote in the elections.\n","green", attrs=["blink"])

def draw(lista):
  count = 0
  while (count < 5):
    lista.append(randint(0,10))
    count+=1
  
  print("Draw 5 values of list: ", end="")   
  for i in range(len(lista)):  
    print(lista[i], end= " ", flush=True)
    sleep(0.5)
    count+=1
  print()  

def some(lista):
  soma = 0
  count = 0
  while (count < len(lista)):
    if lista[count] % 2 == 0:
      soma += lista[count]
    count+=1
  print(f"Adding the even numbers {lista} have {soma}.")    


  

