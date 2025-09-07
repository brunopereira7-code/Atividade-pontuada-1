#Uma financeira usa o seguinte critério para conceder empréstimos: o valor total do empréstimo 
#deve ser até dez vezes o valor da renda mensal do solicitante, e o valor da prestação deve ser no máximo
# 30% da renda mensal do solicitante. Escreva um programa que leia a renda mensal de um solicitante, 
#o valor total do empréstimo solicitado e o número de prestações que o solicitante deseja pagar e
# informe se o empréstimo pode ou não ser concedido.

import os 
os.system("cls") 

valor_emprestimo=float(input("Digite o valor do emprestimo:"))
renda_mensal=float(input("digite sua renda mensal:"))
numero_prestacoes=float(input("Quantas prestaçoes deseja pagar:"))

valor_prestaçao=0.30

if renda_mensal < valor_emprestimo:
    print("Emprestimo nao concebido")
    
elif renda_mensal> valor_emprestimo:
    print("Emprestimo concebido") 

else: 
    print("seus dados nao ta") 

print("\tVolte sempre")