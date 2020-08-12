from termcolor import colored, cprint
from random import randint
from emoji import emojize
from time import sleep
'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''

def play():
  exercise()

  print(emojize("Your car is passing on the radar...  :red_car: ", use_aliases=True))
  sleep(2)
  
  km_max = 80
  km = randint(10,180)
  km_exceed = km - km_max

  if (km > 80):
    print(emojize(f":rotating_light:  You exceeded the allowed limit in {km_exceed}Km.:rotating_light: ", use_aliases=True))
    cprint(colored(f"   You will pay a fine of R${km_exceed*7}   ", "white", "on_yellow"))
  else:
    print(colored("Have a nice day. Drive safe!", "green"))  

def exercise():
  print("Write a program to reads the speed of a car. If it exceed 80Km/h, show a mensage saying that it was taxed. The fine will cost R$ 7.00 for each Km above the limit.\n")  
