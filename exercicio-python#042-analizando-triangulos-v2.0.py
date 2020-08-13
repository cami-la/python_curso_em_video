from termcolor import colored, cprint

'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo, e classifique em:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

def play():
  exercise()

  triangle = yes_triangle()

  if (triangle[0] == triangle [1] == triangle[2]):
    print("EQUILÁTERO!")
  elif (triangle[0] != triangle[1] != triangle[2]):
    print("ESCALENO!")
  else:
    print("ISOSCELES!")  
  


def exercise():
  cprint("""Develop a program that reads the length of three straight ans say to user if they can or cannot form a triangle and sort on:
  - EQUILATERAL: Every side equal
  - ISOSCELES: two side equal, one different
  - SCALENE: every side differentes  
  ""","green", attrs=["blink"])

def yes_triangle():

  sizes_triangle = []
  for i in range(3):
    size = int(input(f"Type the {i+1}º size of the triangle: "))
    sizes_triangle.append(size)

  order_sizes = sorted(sizes_triangle)

  if ((order_sizes[0] < order_sizes[1] + order_sizes[2]) and (order_sizes[0] > order_sizes[2] - sizes_triangle[1])):
    print("This is a triangle", end=" ")
    return order_sizes
  else:
    print("it isnt' a triangle")    

 
