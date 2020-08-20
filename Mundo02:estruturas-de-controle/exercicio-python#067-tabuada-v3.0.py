from termcolor import cprint
'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
'''

def play():
  exercise()

  stop = False

  while(not stop):
    print("-"*30)
    number = int(input("Type a number to multiplication: "))
    print("-"*30)
    if number < 0:
      break   
    
    for i in range(11):
      print(f"{number} x {i:2} = {number*i:2}")
  print("Program Multiplication is finish! Check back often.")    

def exercise():
  cprint("Make a program to shows the multiplication of several numbers, one at a time, to each value typed by user. The program will should be break when the number asked to be negative.","green", attrs=["blink"])
