from termcolor import colored, cprint

'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

def play():
  exercise()

  weight = float(input("Type the weight: (kg) "))
  height = float(input("Type the heignt: (m) "))

  imc = weight / (height * height)

  if (imc < 18.5):
    print(f"According with your IMC {imc:.1f}, your are UNDER WEIGHT.")
  elif (imc <= 25):
    print(f"According with your IMC {imc:.1f}, your are IDEAL WEIGHT.")
  elif (imc <= 30):
    print(f"According with your IMC {imc:.1f}, your are OVERWEIGHT.") 
  elif (imc <= 40):
    print(f"According with your IMC {imc:.1f}, your are OBESITY.")     
  else:  
    print(f"According with your IMC {imc:.1f}, your are MORBID OBESITY.") 

def exercise():
  cprint("""Develop a logic that reads the weight and height of a person, calculate your IMC and show its status, according with the table below:
  - IMC below 18,5: under weight
  - between 18,5 and 25: ideal weight
  - 25 up to 30: overweight
  - 30 up to 40: obesity
  - above 40: morbid obesity\n""","green", attrs=["blink"])
