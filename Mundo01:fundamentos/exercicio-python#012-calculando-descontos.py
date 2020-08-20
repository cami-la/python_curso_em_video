from termcolor import colored, cprint
'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

def play():
  exercise()

  price = float(input("Price of the product: R$"))

  #desconto de 5% é: 1 - 0.05
  print(f"The new price with discount is R${price*0.95}")

def exercise():
  cprint("Make a algorithm to read the price of the product and show its new price, with 5% discount.\n","green", attrs=["blink"])  
