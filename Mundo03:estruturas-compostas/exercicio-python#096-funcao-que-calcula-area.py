from termcolor import cprint
'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
def play():
  exercise()
  print(" Terrain control ")
  print("-----------------")
  area(width = float(input("Width(m): ")), length = float(input("Length(m): ")))


def exercise():
  cprint("Make a program that has a function called area (), that takes the dimensions of a rectangular terrain (width and length) and shows the area of ​​the terrain.\n","green", attrs=["blink"])

def area(width, length):
  print(f"The area of terrain {width}x{length} is {width*length}m².")
  
