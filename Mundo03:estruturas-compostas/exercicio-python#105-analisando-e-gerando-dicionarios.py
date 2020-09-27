from termcolor import cprint
'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''

def play():
  exercise()

  print(notes(6,8,8, sit=True))

  help(notes)



def exercise():
  cprint("""Make a program that has a grades function () that can receive multiple grades from students and will return a dictionary with the following information:

- Number of notes
- The highest grade
- The lowest grade
- The class average
- The situation (optional)

Also add the docstrings of this function for consultation by the developer.\n""","green", attrs=["blink"])

def notes(*note, sit=False):
  """
  -> Function to analyze grades and situation of several students.
  :param note: one or more student grades (accepts several)
  :param sit: optional value, indicating whether or not to add the situation
  :param return: dictionary with various information about the class situation
  """
  r = {}
  
  r["amount_note"] = len(note)
  r["biggest"] = max(note)
  r["smallest"] = min(note)
  r["avanger"] = sum(note)/r["amount_note"]
  
  if sit:
    if r["avanger"] >= 7:
      r["situation"] = "Approved" 
    else:
      r["situation"] = "Fail" 

  return r


