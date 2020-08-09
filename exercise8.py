'''
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e em milimetros.
'''

def play():

  exercise()

  meter = float(input("Type the value in meter: "))

  print(f"Meter: {meter:.0f}m - Centimeter: {meter*100:.0f}cm - Milimeter: {meter*1000:.0f}mm")

def exercise():
  print("Write a program to read a value in meters and show converted in centimeters and milimeters.\n")
