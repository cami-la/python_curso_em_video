from termcolor import cprint
from random import randint
'''
O computador vai "pensar" em um número entre 0 e 10. O jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

def play():
  exercise()
  '''
  computer = randint(0,10)
  gamer = int(input("Type a number between 0 and 10: "))
  print(f"Computer {computer} x {gamer} gamer")
  while (gamer not in range(10)):
    gamer = int(input("Type a number between 0 and 10: "))

  try_hit = 1
  while (not gamer == computer):
    try_hit += 1
    computer = randint(0,10)
    gamer = int(input("Type a number between 0 and 10: "))
    print(f"Computer {computer} x {gamer} gamer")
    while (gamer not in range(10)):
      gamer = int(input("Type a number between 0 and 10: "))
  print(f"You won! Number of try {try_hit}.")
  '''

  hit = False

  try_hit = 0

  while (not hit):
    try_hit +=1
    computer = randint(0,10)
    gamer = int(input("Type a number between 0 and 10: "))
        
    while (gamer not in range(11)):
      print("Invalid try! Try again.")
      try_hit +=1
      print() 
      gamer = int(input("Type a number between 0 and 10: "))
    
    print(f"Computer {computer} x {gamer} gamer")  

    if (gamer < computer):
      print("Your kick was smaller, try again!\n")
    elif (gamer > computer):
      print("Your kick was bigger, try again!\n")
    else:  
      hit = True
  print(f"You won! Number of try {try_hit}.")     
  

def exercise():
  cprint("The computer will 'think' in one number between 0 and 10. The gamer will try guess up to hit, showing at the end how many kick were necessary to won!\n","green", attrs=["blink"])
