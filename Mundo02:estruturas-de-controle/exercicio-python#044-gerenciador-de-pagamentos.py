from termcolor import colored, cprint

'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

def play():
  exercise()
  print("{:=^40}".format(" CAMILA STORE "))
  
  price_product = float(input("Type the price of the purchase: "))
  
  print("""\n  PAYMENT TERMS  
  [1] cash/check: 10% discount
  [2] cash on the card: 5% discount
  [3] up to 2x on the card: formal price
  [4] 3x or more on the card: 20% interest
  """, end="")
  payment_terms = int(input("CHOICE THE PAYMENT TERMS: "))
  print("\n", end=" ")
  

  if (payment_terms == 1):
    discount = price_product*0.10
    total = price_product*0.9
    print(f"You get a R${discount} of discount.")
  elif (payment_terms == 2):
    discount = price_product*0.05
    total = price_product*0.95 
    print(f"You get a R${discount} of discount.")
  elif (payment_terms == 3):
    discount = 0
    total_installments = int(input("Type the total installments: "))
    total = price_product*1    
    installments = False
    while(not installments):
      if (total_installments == 1 or total_installments == 2):
        print(f"Your purchase was divided into {total_installments} x R${total/total_installments}")
      else:
        print("Invalid Installment. Try again!", end = " ")
      break 
  elif (payment_terms == 4):
    discount = 0
    total_installments = int(input("Type the total installments: "))
    total = price_product*1.2
    
    installments = False
    while(not installments):
      if (total_installments >= 3):
        print(f"Your purchase was divided into {total_installments} x R${total/total_installments}")
      else:
        print("Invalid Installment. Try again!", end = " ")
      break 
  else:
    total = price_product
    print("INVALID PAYMENT TERMS ")
         
  print(f"Total price is R${total}")

def exercise():
  cprint("""Develop a program that calculate the amount to be paid for a product, considering its normal price and payment terms:
  - cash / check: 10% discount
  - cash on the card: 5% discount
  - up to 2x on the card: formal price
  - 3x or more on the card: 20% interest.\n""","green", attrs=["blink"])
