from list_of_exercises.exercise115.libs.interface import *
from list_of_exercises.exercise115.libs.file import *
from time import sleep

def play():
  file = "cursoemvideo.txt"

  if not exist_file(file):
      create_file(file)

  while True:
      result = menu(["Display registred people", "Register New Person", "Exit the System"])
      if result == 1:
          # To List the contect of a file.
          read_file(file)
      elif result == 2:
          # Register a new person
          header("NEW REGISTER")
          name = str(input("Name: "))
          age = read_integer("Age: ")
          register(file, name, age)
      elif result == 3:
          print("Check Back Often!")
          break
      else:
          print("\033[31mErro! Type a valid option.\033[m")
      sleep(2)

    
