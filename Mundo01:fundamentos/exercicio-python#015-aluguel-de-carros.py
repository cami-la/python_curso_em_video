from termcolor import colored, cprint
'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

def play():
  exercise()

  kilometers = float(input("Type the how many kilometers car has driven: "))
  days = int(input("Type the how much days it has been rented: "))

  price_kilometers = kilometers*0.15
  price_days = days*60

  print(f"\nThe price to pay by {kilometers}km is R${price_kilometers} and {days} days is R${price_days}. Total R${price_kilometers + price_days}.")

def exercise():
  cprint("Write a program that asks how many kilometers a car has driven and the number of days it has been rented. Calculate the price to pay, knowing that the car costs R$60 per day and R$ 0.15 per km driven.\n","green", attrs=["blink"])
