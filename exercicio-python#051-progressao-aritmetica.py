from termcolor import cprint
'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
'''

def play():
  exercise()

  n1_pa = int(input("Type the first number of the PA: ")) 
  reason_pa = int(input("Type the reson of the PA: "))
  
  for i in range(10):
    term_pa = n1_pa + (i-1)*reason_pa
    if (term_pa >= 0):
      print(f"{term_pa}", end=" → ")
  print("end")  



def exercise():
  cprint("Develop a program to read the first term of an arithmetic progression and its reason. The end, show the 10 firsts terms this progression.\n","green", attrs=["blink"])
