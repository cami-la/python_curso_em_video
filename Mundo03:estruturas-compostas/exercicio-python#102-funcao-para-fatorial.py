from termcolor import cprint
'''
Crie um programa que tenha uma função fatorial () que receba dois parâmetros: o primeiro que indica o número a ser calculado e outro chamado show, que será um valor lógico (opcional) indicando se será ou não o processo de cálculo fatorial mostrado na tela.
'''
def play():
  exercise()

  number = int(input("Number to calculate the factorial: "))

  print(factorial(number,True))
  help(factorial)

def exercise():
  cprint("Create a program that has a factorial function () that receives two parameters: the first one that indicates the number to be calculated and another one called show, which will be a logical value (optional) indicating whether or not the factorial calculation process will be shown on the screen.\n","green", attrs=["blink"])

def factorial(num, show=False):

  factorial = 1
  
  if (show):
    print(f"{num}! = ", end = "")

  for i in range(num, 0, -1):
    if (show):
      if (i != 1):
        print(i, end=" x ")
      else:
        print(i, end=" = ")
    factorial *= i
  
  return factorial 

