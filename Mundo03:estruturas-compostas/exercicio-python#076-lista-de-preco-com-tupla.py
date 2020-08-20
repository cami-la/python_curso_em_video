from termcolor import cprint
'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

def play():
  exercise()

  prices_list = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

  print("-"*40)
  print(f"{'PRICE LISTING':^40}")
  print("-"*40)

  for index in range(len(prices_list)):
    if (index % 2 == 0):
      print(f"{prices_list[index]:.<30} R$", end="")
    else:
      print(f"{prices_list[index]:>7.2f}")
  
  print("-"*40)

def exercise():
  cprint("Create a program that reads a single tuple with product's names and its respective prices, in the sequence. At the end, show a price listing, organizing the data in tabular form.\n","green", attrs=["blink"])
