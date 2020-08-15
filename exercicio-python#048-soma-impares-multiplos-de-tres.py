'''
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

def play():
  exercise()
  
  odd_multiples_three = []
  
  for i in range(1,501):
    
    if (i % 3 == 0 and i % 2 != 0):
      print(i, end = " ")
      odd_multiples_three.append(i)
    
  print(f"\nThe sum {len(odd_multiples_three)} is: {sum(odd_multiples_three)}")    
  print(contador)

def exercise():
  cprint("Make a program that calculates the sum between all numbers that are multiples of three and that are in the range of 1 to 500.\n","green", attrs=["blink"])
