from termcolor import colored, cprint
'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

def play():
  exercise()

  notes = []
  for i in range(2):
    note = float(input(f"Type the {i+1} note: "))
    notes.append(note)

  #média: soma de todas as notas dividido pela quantidade de notas
  average = sum(notes)/len(notes)

  if (average >= 7):
    print(f"Congratulations, your average is {average}. So, YOU ARE APPROVED!")
  elif (7 > average >= 5):
    print(f"Your average is {average}. So, YOU ARE IN RECUPERATION!")
  else:
    print(f"Your average is {average}. So, YOU ARE DISAPPROVED!")

def exercise():
  cprint("""Creat a program that reads two notes of a student and calculate your average showing a menssage in the end, according with a average:
  - Average under of 5.0: disapproved
  - Average between 5.0 and 6.9: recuperation
  - Avarage above 7.0 or more: approved""","green", attrs=["blink"])


