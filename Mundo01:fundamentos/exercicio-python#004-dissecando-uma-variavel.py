from termcolor import colored, cprint
'''
Faça um programa que leia algo do teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele.
'''

def play():
  exercise()

  #a string word se comporta como um objeto que tem suas caracteristicas e métodos. Por isso pode ser chamado com o .
  word = input("Type the word to be evaluated: ")

  print("\nThe type this word is: ", type(word))
  print("Does this word has only spaces?", word.isspace())
  print("Does this word is a digit?", word.isdigit())
  print("Does this is alphabetic?", word.isalpha())
  print("Does this is alphanumeric?", word.isalnum())
  print("Does this is capital?", word.isupper())
  print("Does this is lowercase?", word.islower())
  print("Does this word begin with capital letter?", word.istitle())

def exercise():
  cprint("Faça um programa que leia algo do teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele.\n","green", attrs=["blink"])
