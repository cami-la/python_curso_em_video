from math import hypot #no módulo math tem uma função para calcular a hipotenusa.
'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''

def play():
  exercise()

  cathetu_opposite = float(input("Type the value of legth of cathetu opposite: "))
  cathetu_adyacente = float(input("Type the value of legth of cathetu adyacente "))

  #fórmula para calcular a hipotenusa de um triângulo retângulo.
  hypotenuse = ((cathetu_opposite**2) + (cathetu_adyacente**2)) ** 0.5

  hypothenuse2 = hypot(cathetu_opposite, cathetu_adyacente)

  print(f"The cathetu opposite is {cathetu_opposite}, the cathetu adyacente is {cathetu_adyacente} and the hypotenuse is {hypotenuse:.2f}")
  print(f"The cathetu opposite is {cathetu_opposite}, the cathetu adyacente is {cathetu_adyacente} and the hypotenuse is {hypothenuse2:.2f}")

def exercise():
  print("Make a program to read the length of cathetu opposite and of cathetu adyacente of the rectangle triangle. Calculate and show the length hypotenuse.\n")
