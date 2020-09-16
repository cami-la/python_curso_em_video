'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

def play():
  #exercise()
  
  biggest(2,4,9,5,7,1)
  biggest(4,7,0)
  biggest(1,2)
  biggest(1)
  biggest()

def exercise():
  cprint("Make a program that has a function called greater (), that receives several parameters with integer values. Your program has to analyze all the values ​​and say which one is the highest.\n", "green", attrs=["blink"])

def biggest(*numbers):
  print("-="*30)
  count = 0
  biggest = 0
  while(count < len(numbers)):
    print(numbers[count], end=" ")

    if (count == 0):
      biggest = numbers[count]
    else:
      if (numbers[count] > biggest):
        biggest = numbers[count]
    count+=1
    
  print(f"Were inform {count} values")
  print(f"The biggest number is {biggest}.")  
