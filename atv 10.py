#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível 
#(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente, 
#sabendo-se que o preço do litro da gasolina é R$ 6,59 e o preço do litro do álcool é R$ 3,79.


import os 
os.system("cls") 

print("""
Combustível Quantidade Vendida Desconto por Litro
Alcool   -  ate 25 litros       -     10%
Alcool   -  acima 25 litros     -     20%
Gasolina -  ate 25 litros       -     15%
Gasolina -  acima 25 litros     -     30%
      
    """)  

combustivel=input("Qual voce quer álcool ou gasolina:")
litros=int(input("Quantos litros voce quer:"))

preco_por_litro=0
desconto=0



match combustivel .strip() .lower():
    case"gasolina":
        preco_por_litro= 6.59 
        if litros <= 25:
            desconto= 0.15

        elif litros >= 25:
            desconto=0.20

    case"alcool":
        preco_por_litro=3.79
        if litros <= 25:
            desconto=0.15 

        
        elif litros >=25:
            desconto=0.30

    case _:
        print("digita umas das opçoes acima")


if preco_por_litro >0:

    total = litros * preco_por_litro
    valor_desconto = total * desconto
    total_a_pagar = total - valor_desconto


print(f"o seu combustivel é {combustivel}")
print(f"o seu litro é {litros}")
print(f"o preço por litro é {preco_por_litro}")
print(f"o preço total é {total}")
print(f"o desconto é {desconto}) R$ {valor_desconto:.2f}")
print(f"o seu valor total é {total_a_pagar:.2f}")


    



    



