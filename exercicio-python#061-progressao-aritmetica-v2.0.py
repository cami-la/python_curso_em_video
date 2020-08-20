from termcolor import cprint
'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão, usando o laço de repetição while.
'''

def play():
  exercise()

  #an = a1 + (n-1)*r
  a1 = int(input("Type the first PA number: "))
  reason_pa = int(input("Type the PA reason: "))

  print("\nPA GENERATOR")
  print("-="*10)
  print(f"The first PA number: {a1}")
  print(f"The PA reason: {reason_pa}")
  '''
  count = 0
  while(count <= 10-1):
    pa = a1 + (count)*reason_pa
    count +=1
    print(f"{pa}", end="")
    print(" → ", end="")
  print("end")
  '''
  for count in range(10):
    pa = a1 + (count)*reason_pa
    print(f"{pa}", end="")
    print(" → ", end="")
  print("end")    
    

def exercise():
  cprint("Develop a program to reads the first term and the reason of the PA. At the and, show the 10 firsts terms this progression, using the while loop.\n","green", attrs=["blink"])
