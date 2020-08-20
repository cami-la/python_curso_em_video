from termcolor import cprint
'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

def play():
  exercise()

  numbers = []
  count = 0
  stop = False
  
  while (not stop):
    number = int(input("Type the integer number [999 to stop]: "))
    if (number != 999):
      numbers.append(number)
    else:
      stop = True
  print(f"You typed {len(numbers)} numbers and the add between them is {sum(numbers)}.")      

def exercise():
  cprint("Creat a program to reads several integers numbers by keyboard. The program only will stop when the user type the value 999, that is the condition of stoped. At the end, show how many numbers were typed and wich was the add between them. (disregarding the flag)","green", attrs=["blink"])
