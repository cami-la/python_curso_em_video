from termcolor import colored

'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

def play():
  exercise()

  distance = float(input("How far will you travel on this trip? "))

  if (distance <= 200):
    print(colored(f"The ticket price is {distance * 0.5}", "cyan"))
  else:
    print(colored(f"The ticket price is {distance * 0.45}", "cyan"))  

def exercise():
  cprint(colored("Develop a program that asks for the distance of a trip in Km. Calculate the ticket price, charging R $ 0.50 per Km for trips of up to 200 km and R $ 0.45 for longer trips.\n", "green", attrs=["blink"])) 
