from termcolor import cprint
'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

def play():
  exercise()

  names = []
  ages = []
  woman_names = []
  man_names = []
  woman_ages = []
  man_ages = []
  
  for i in range(4):
    print("-"*5, f"{i+1}º PERSON ", "-"*5)
    
    name = str(input("Name: "))
    names.append(name)
    age = int(input("Age: "))
    ages.append(age)

    sex = str(input("Sex [M/F]: ")).strip().upper()
    
    if (sex == "F"):
      woman_names.append(name)
      woman_ages.append(age)
    else:  
      man_names.append(name)
      man_ages.append(age)
    
  print(f"\nThe average age of the group is {sum(ages)/len(ages)}")
  print(f"The older man is {man_names[man_ages.index(max(man_ages))]}")
  
  bigger_20 = 0
  for age in woman_ages:
    if age < 20:
      bigger_20 += 1

  print(f"There are {bigger_20} women over of twenty years old.")    


def exercise():
  cprint("""Develop a program to reads the name, age and sex of four peoples. At the end of program, show: 
  - the average age of the group,
  - wich the name of the older man 
  - how many women have less than twenty years.\n""","green", attrs=["blink"])
