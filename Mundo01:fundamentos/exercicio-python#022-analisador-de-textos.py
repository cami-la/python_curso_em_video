'''
Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
'''

def play():
  exercise()

  #aqui o programa vai capturar o nome completo e retirar os espaços na frente a atraz da string caso tenha e colocar as primeiras letras dos nomes em maiúsculo.
  full_name = str(input("Type your full name: ")).strip().title()
  
  print(f"Your full name is: {full_name}")
  print(f"Your full name with every letter capitalize: {full_name.upper()} ")
  print(f"Your full name with every letter lowercase: {full_name.lower()} ")
  print(f"Your full name without spaces: {full_name.strip()} ")
  #para sabermos a quantidade de espaços em branco que existe na string, usamos .count()
  amount_space_between_words = full_name.count(" ")
  #para saber o comprimento de uma string, usamos a função len(). Então para saber a quantidade de letras sem o espaços, é só subtrair a quantidade de espaços do comprimento total da string.
  print(f"Your full name has {len(full_name) - amount_space_between_words} letters. ")


  '''
  Para saber a quantidade de letras do primeiro nome, é só encontra o primeiro espaço em branco com o .find().
  Esse método diz a posição desse espaço que consequentemente é equivalente a quantidade de letras do primeiro nome.
  '''
  position_of_first_empty_space = full_name.find(" ")
  print(f"Your first name has {position_of_first_empty_space} letters. ")

  
  #Também podemos usar o método .split(). Ele separa as palavras sem os espaços e joga numa lista.
  names_separated = full_name.split()
  print(names_separated)
  print(f"\nYour first name is {names_separated[0]} and its has {len(names_separated[0])} letters.")


def exercise():
  cprint("""Create a program to read the name's person and show:)
  - The name with all the letters capitalize and lowcase
  - How many letters in all (without spaces)\n""","green", attrs=["blink"]) 
