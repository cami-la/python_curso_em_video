'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

def play():
  exercise()

  person_name = str(input("Type your full name: ").upper().strip())

  if ("SILVA" in person_name):
    print("Yes, your name has 'SILVA'.")
  else:
    print("No, your name hasn't 'SILVA'.")  

def exercise():
  print("Created a program to read the name's person and say if its has 'SILVA' in the name.\n")
