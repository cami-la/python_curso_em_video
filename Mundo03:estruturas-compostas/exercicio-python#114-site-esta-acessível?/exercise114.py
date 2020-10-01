'''
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''
import urllib
import urllib.request
from termcolor import cprint

def play():
  exercise()
  try:
      site = urllib.request.urlopen("http://www.pudim.com.br")
  except urllib.error.URLError:
      print("\033[31mGave Error\033[m")
  else:
      print("Ok!")

def exercise():
  cprint("Create Python code that tests whether the pudding site is accessible from the computer used.\n", "green", attrs=["blink"])
