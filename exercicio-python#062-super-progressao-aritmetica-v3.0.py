from termcolor import cprint
'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão, usando o laço de repetição while. 
Depois, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos. 
'''

def play():
  exercise()

  a1 = int(input("Type the first PA number: "))
  reason_pa = int(input("Type the PA reason: "))
  terms_pa = 10

  print("\nPA GENERATOR")
  print("-="*10)
  print(f"The first PA number: {a1}")
  print(f"The PA reason: {reason_pa}")
  total = 0
  finish = False
 
  while (not finish):
    total = total + terms_pa
    for count in range(terms_pa):
      pa = a1 + count*reason_pa
      print(f"{pa}", end="")
      print(" → ", end="")
    print("pause")
    a1 = a1 + terms_pa*reason_pa    
    
    terms_pa = int(input("How much terms do you want show more? "))
    if (terms_pa == 0):
      print(f"\nProgression ended with {total} terms")
      finish = True


def exercise():
  cprint("Develop a program to reads the first term and PA reason. At the end, show the 10 firts terms this progression, using the loop while. After, ask to user if he wants to show more some terms. The program will end when he says that wants to show 0 terms.\n","green", attrs=["blink"])
