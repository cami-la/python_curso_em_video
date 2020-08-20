from termcolor import cprint
'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

def play():
  exercise()

  words = ("LEARN", "PROGRAM", "LINGUAGE, ""PYTHON", "COURSE", "FREE", "STUDY", "PRATICE", "WORK", "LABOR", "PROGRAMMER", "FUTURE")

  for word in words:
    cprint(f"\nOn the word {word} we have: ", end=" ")
    for letter in word:
      if letter.lower() in "aeiou":
        print (f"{letter}", end=" ")

    
    

def exercise():
  cprint("Create a program that has a tuple with several words (don't use accents). After this, you must show, to each word, what are its vowels.\n","green", attrs=["blink"])
