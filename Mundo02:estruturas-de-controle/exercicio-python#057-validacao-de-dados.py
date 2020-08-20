from termcolor import cprint
'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

def play():
  exercise()

  '''
  correct_sex = False
  
  while(not correct_sex):
    sex = str(input("Type the sex: ")).strip().upper()
    if (sex == "M"):
      print("Sex M registered successful")
      break
    elif (sex == "F"):
      print("Sex M registered successful")
      break
    else:
      continue  
  '''

  sex = str(input("Type the sex: ")).strip().upper()
  while (sex not in "MF"):
    sex = str(input("Type the sex: ")).strip().upper()
  print(f"Sex {sex} registered successful")  

def exercise():
  cprint("Make a program to read the sex of a person, but only accept the values 'M' or 'F'. If be wrong, ask that type again up to have a correct value.\n","green", attrs=["blink"])


