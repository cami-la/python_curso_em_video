from termcolor import cprint
'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''

def play():
  exercise()

  phrase = str(input("Type a phrase: ")).strip(" ").upper()

  phrase = phrase.replace(" ","")

  inverted_phrase = phrase[::-1]

  if (phrase == inverted_phrase):
    print("This phrase is a PALINDROME:", end=" ")
    print(f"{phrase} is equal a {inverted_phrase}")
  else:
    print("This phrase isn't a PALINDROME:", end=" ")
    print(f"{phrase} is different a {inverted_phrase}")  

def exercise():
  cprint(f"Create a program to reads a any phrase and says if its is a palindrome, disregarding the spaces.","green", attrs=["blink"])
