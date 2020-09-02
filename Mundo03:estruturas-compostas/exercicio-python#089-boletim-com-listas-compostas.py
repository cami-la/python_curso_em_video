from termcolor import cprint
'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

def play():
  exercise()

  listing_students = []
  list_temp = []

  while(True):
    name = str(input("Name: ")).capitalize().strip()
    note1 = float(input("Note 1: "))
    note2 = float(input("Note 2: "))
    averange = (note1 + note2)/2
    
    list_temp = [name, [note1,note2], averange]
    listing_students.append(list_temp[:])
    list_temp.clear()

    to_continue = " "
    while(to_continue not in "YN"):
      print()
      to_continue = str(input("Do you want to continue? [Y/N] ")).upper().strip()
    if to_continue == "N":
      break
  print("-"*22)
  print(f"{'No.':<4}{'Name':<10}{'Averange':>8}")
  print("-"*22)
  for i in range(len(listing_students)):
    print(f"{i:<4}{listing_students[i][0]:<10}{listing_students[i][2]:>8}")

  while(True):
    
    option = int(input("Which student do you want to show grades? [999 stop] "))
    if (option == 999):
      print("\nFinishing...")
      break
   
    if (option <= len(listing_students)-1):
      print(f"The grades of student {listing_students[option][0]}: {listing_students[option][1]}")
    
  print(">>> Check back often <<<")


def exercise():
  cprint("Create a program that reads the name and two notes of several students and stores everything in a compound list. At the end, show a bulletin containing the average of each one and allow the user to show the grades of each student individually.\n","green", attrs=["blink"])
