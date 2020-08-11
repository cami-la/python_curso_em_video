'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''

def play():
  exercise()

  full_name = str(input("Type your full name: ")).title().strip()

  position_first_name = full_name.find(" ")
  position_last_name = full_name.rfind(" ")

  print(f"Your first name is {full_name[:position_first_name]} and your last name {full_name[position_last_name + 1:]}.")

  name = full_name.split()

  print(f"Your first name is {name[0]} and your last name {name[len(name)-1]}.")

def exercise():
  print("Make a program to read the full name of a person, show then the first and the last name separately.\n")

