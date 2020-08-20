'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
'''

def play():
  
  print("-"*30)
  print("      LOJA SUPER BARATÃO      ")
  print("-"*30)

  products = []
  prices = []
  price_more_than_1000 = []

  end = False

  while(not end):
    product = str(input("Product's name: ")).upper().strip()
    products.append(product)    
    
    price = float(input("Price: R$"))
    prices.append(price)
    if (price > 1000):
      price_more_than_1000.append(price)

    to_continue = " "
    while(to_continue not in "YN"):
      to_continue = str(input("Do you want to continue? [Y/N] ")).upper().strip()
    
    if (to_continue == "N"):
      print("-"*15, "THE END", "-"*15)
      end = True
  
  print(f"The total amount spend on the purchase is {sum(prices)}")
  print(f"The {len(price_more_than_1000)} products cost more than R$1000.")
  print(f"The {products[prices.index(min(prices))]} was the product more cheap.")






def exercise():
  cprint(""" Make a program to reads the name and the price of several productos. The program should be asks if the user will go to continue or don't. At the and, show:
A) what is the total amount spent on the purchase
B) How many products cost more than R$1000
C) What is the name of the product more cheap\n ""","green", attrs=["blink"])

