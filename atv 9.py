

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
