from termcolor import colored, cprint
'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

def play():
  exercise()

  sizes_triangle = []
  for i in range(3):
    size = int(input(f"Type the {i+1}º size of the triangle: "))
    sizes_triangle.append(size)

  order_sizes = sorted(sizes_triangle)

  if ((order_sizes[0] < order_sizes[1] + order_sizes[2]) and (order_sizes[0] > order_sizes[2] - sizes_triangle[1])):
    print("This is a triangle.")
  else:
    print("it isnt' a triangle")  

def exercise():
  cprint("Develop a program that reads the length of three straight and say to user if them can or can't form a triangle.\n","green", attrs=["blink"])
