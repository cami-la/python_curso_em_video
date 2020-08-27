from termcolor import cprint
'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

def play():
  exercise()
  
  expression = str(input("Type the expression: "))
  stack = []

  
  for simbol in expression:
    if (simbol == "("):
      stack.append("(")
    elif (simbol == ")"):
      if len(stack) > 0:
        stack.pop()
      else:
        stack.append(")")
        break

  if len(stack) == 0:
    print("This expression is valid!")
  else:
    print("This expression is invalid!")          

  
  
def exercise():
  cprint("Create a program where the user inserts any expression that uses parentheses. Your application should be analyzing whether the expression has open or closed parentheses in the correct order.\n","green", attrs=["blink"])
