#Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário
#Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que:
#Se quantidade <= 5, o desconto será de 2%.
#Se quantidade > 5 e quantidade <= 10, o desconto será de 3%.
#Se quantidade > 10, o desconto será de 5%.
import os 
os.system("cls")

produto=input("digite o seu produto:")
quantidade=float(input("digite sua quantidade:"))
preço_unitario=1.30

total=quantidade*preço_unitario


if quantidade <= 5:
    desconto=0.2

elif quantidade >5:
    desconto=0.3

elif quantidade >= 10:
    desconto=0.5 

    total_pagar=total - desconto 



print(f"\nproduto é {produto}")
print(f"a quantidade {quantidade}")
print(f"preço unitario: R$ {preço_unitario:.2f}")
print(f"total: R$ {total:.2f}")
print(f"desconto é {desconto:.2f}")
print(f"o total é {Total}")