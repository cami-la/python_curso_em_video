from termcolor import colored, cprint
from random import randrange, choice, shuffle

'''
Um professor escolhe quatro dos seus alunos para apresentar um trabalho. Faça um programa que ajude ele, lendo os nome dos alunos e escrevendo na tela a ordem aleatória dos alunos escolhidos.
'''

def play():
  exercise()

  #função para pedir o nome dos alunos
  students = ask_name_students()
  
  #função para exibir o nome dos alunos escolhidos
  print("\nList of chosen students")
  print(students)
  
  #embaralhando a própria lista.
  shuffle(students)
  
  #exibindo a nova lista
  print("\nStudent's list by order of a presentation:")
  show_name_students(students)
  


def exercise():
  cprint("A teacher choice his four of students to introduce a work. Make a program to help him, writing the name's students on the screen the order random to introduce the work.\n","green", attrs=["blink"])

def ask_name_students():
  students = []
  for i in range(0, 4):
    student = str(input(f"Type the {i+1}º name's student: "))
    student = student.capitalize()
    students.append(student)
  return students  

def show_name_students(students):
  print(students)
  print("\nThe order of presentation will be:")
  index = 0
  for i in students:
    print(f" {index + 1}º is {students[index]}")
    index = index + 1
