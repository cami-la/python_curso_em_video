from termcolor import cprint
'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

def play():
  exercise()
  
  people = []

  person = {}
  
  some = 0;

  
  while(True):
    person["name"] = str(input("Name: "))
    
    person["gender"] = str(input("Gender [M/W]: ")).upper().strip()
    while(person["gender"] not in "MW"):
      person["gender"] = str(input("Enter the gender between [M/W]: ")).upper().strip()

    person["age"] = int(input("Age: "))
    some += person["age"]

    people.append(person.copy())
    
    to_continue = str(input("Do you want to continue? ")).upper().strip()
    while(to_continue not in "NY"):
      to_continue = str(input("Do you want to continue? ")).upper().strip()
    if to_continue == "N":
      break  
  print("-="*30)

  print(f"We have {len(people)} people registred.")
  avanger = some/len(people)
  print(f"The averange age is {avanger:.2f}")
  print(f"Registered women were ", end="")
  for register in people:
    if (register["gender"] == "W"):
      print(f"{register['name']}", end =" ")
  print()
  print("list of people who are above average", end="")
  for register in people:
    if (register["age"] >= avanger):
      print("    ")
      for k, v in register.items():
        print(f"{k} = {v};", end = " ")
      

def exercise():
  cprint("""Create a program that reads the name, sex and age of several people, saving each person's data in a dictionary and all dictionaries in a list. At the end, show:
A) How many people were registered
B) Average age
C) A list of women
D) A list of people above the average age\n""","green", attrs=["blink"])

