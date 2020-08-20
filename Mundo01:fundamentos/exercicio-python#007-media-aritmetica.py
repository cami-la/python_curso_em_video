from termcolor import colored, cprint
'''
Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.
'''

def play():
  exercise()

  #aqui foi usado float porque pode ser um número inteiro ou real.
  grade1 = float(input("Type the first grade's student: "))
  grade2 = float(input("Type the second grade's student: "))

  print(f"The student average is {(grade1+grade2)/2:.1f} ")

def exercise():
  print("Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.\n","green", attrs=["blink"])
