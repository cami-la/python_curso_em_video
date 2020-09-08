from termcolor import cprint
'''
Faça um programa que leia nome e média de um aluno,guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''

def play():
  exercise()

  student = {}

  student["name"] = str(input("Type a student's name: "))
  student["averange"] = float(input(f"Type the {student['name']}'s averange: "))

  if (student["averange"] < 7): 
    student["situation"] = "Failed"
  elif (student["averange"] >= 7):
    student["situation"] = "Approved"

  print("="*30)
  for v, k in student.items():
    print(f"The {v} is equals {k}")



def exercise():
  cprint("Make a program that reads name and averange of a student, saving also the situation on the in the dictionary. At the end, show the content of estuture on the screen.\n","green", attrs=["blink"])

