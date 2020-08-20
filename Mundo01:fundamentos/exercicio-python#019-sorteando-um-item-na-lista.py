from termcolor import colored, cprint
from random import randrange, choice
'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''

def play():
  exercise()

  #chamando a função e guardando o retorno em uma variável
  students = save_the_name()
  
  #sorteio. Usamos o método randrang para sortear a posição na lista students entre 0 e a quantidade de alunos.
  raffle = randrange(0, len(students))
  
  #para escolher e exibir o nome do aluno, é só usar o método choice.
  student_name = choice(students)
  '''
  ou para exibir o nome, também pode ser dessa forma:
  student_name = students[raffle]
  '''

  print(f"\nThe sorted student is {student_name.capitalize()} wich was in the {raffle + 1}º position.")  

  

def exercise():
  cprint("A teacher wants to sorted one of the his fours students to clean the board. Make a program to help him, reading the name's students and writing on the screen the name choice.\n","green", attrs=["blink"])  

#função criada para criar uma lista para pedir e salvar os nomes dos alunos
def save_the_name():
  students = []
  for i in range(0,4):
    student = str(input(f"Type the {i+1}º name's student: "))
    students.append(student)
  return students
  
