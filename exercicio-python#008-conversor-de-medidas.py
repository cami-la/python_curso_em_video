from termcolor import colored, cprint
'''
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e em milimetros.
'''

def play():

  exercise()

  meter = float(input("Type the value in meter: "))

  print(f"Meter: {meter:.0f}m - Centimeter: {meter*100:.0f}cm - Milimeter: {meter*1000:.0f}mm")

def exercise():
  cprint("Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e em milimetros.\n" ,"green", attrs=["blink"])
