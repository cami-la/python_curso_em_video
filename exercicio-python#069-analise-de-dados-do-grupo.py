from termcolor import cprint
'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
'''

def play():
  exercise()

  people_over_18_years_old = []
  men = []
  women_more_20_years_old = []
  
  more_people = False

  while(not more_people):
    print("-"*30)
    print("REGISTER ONE PERSON")
    print("-"*30)

    age = int(input("Person's Age: "))
    if (age > 18):
      people_over_18_years_old.append(age)
    
    gender = " "
    while (gender not in "MF"):
      gender = str(input("Person's gender: [M/F] ")).upper().strip()
    if gender == "M":
      men.append(gender)
    elif gender == "F" and age > 20:
      women_more_20_years_old.append(gender)

    print("-"*30)
    to_continue = " "
    while(to_continue not in "YN"):
      to_continue = str(input("Do you want to continue? [Y/N] ")).upper().strip()

    if (to_continue != "Y"):
      more_people = True

  print(f"\nThe total number of people registered with over 18 years old is {len(people_over_18_years_old)}")  
  print(f"Altogether we have {len(men)} men registred")
  print(f"Altogether we have {len(women_more_20_years_old)} women under 20 years old.")





def exercise():
  cprint("""Create a program that reads the age and sex of several people. To each registered person, the program should ask if the user want or don't want to continue. At the and, show:
A) How many people are over 18
B) How many men were registered
C) How many women are under 20 years old \n""","green", attrs=["blink"])
