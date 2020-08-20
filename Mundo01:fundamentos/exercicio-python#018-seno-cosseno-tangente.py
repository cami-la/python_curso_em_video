from termcolor import colored, cprint
from math import radians, sin, cos, tan 
#o math tem o método de calcular o seno, o cosseno e a tangente. Mas fique atento ao detalhe, esses métodos recebem o valor do ângulo em radianto, logo, é necessário converter.
'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

def play():
  exercise()

  angle_in_degree = float(input("Type the angle degraus: "))
  angle_in_radians = radians(angle_in_degree)

  sine = sin(angle_in_radians)
  cosine = cos(angle_in_radians)
  tangent =  tan(angle_in_radians)

  print(f"The sine, cosine and tangent of the angle {angle_in_degree} is successively: {sine:.2f}, {cosine:.2f}, {tangent:.2f}")

def exercise():
  cprint("Make a program to read a any angle and show on the screen the sine, cosine and tangent value this angle.\n","green", attrs=["blink"])
