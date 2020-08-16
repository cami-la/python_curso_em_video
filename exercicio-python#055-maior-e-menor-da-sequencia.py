from termcolor import cprint
'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

def play():
  exercise()

  weights = []

  for i in range(5):
    weight = float(input(f"Type the weight of the {i+1}º people: "))
    weights.append(weight)

  print(f"\nThe bigger weight is {max(weights)}kg and smaller {min(weights)}kg")

def exercise():
  cprint("Make a program to read the weight of five peoples. At the end, show which was the bigger and smaller weight read.\n","green", attrs=["blink"])


