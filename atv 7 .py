import os 
os.system("cls")


fruta = input("Digite sua fruta: ")
quantidade = int(input("Digite a quantidade: "))
preco_unitario = float(input("Digite o preço unitário: "))


total = quantidade * preco_unitario


if quantidade <= 5:
   
    desconto = 0.02  # 2%
elif quantidade > 5 and quantidade <= 10:
    
    desconto = 0.03  # 3%
else: 
    desconto = 0.05  # 5%


valor_desconto = total * desconto
total_a_pagar = total - valor_desconto



print(f"A sua fruta é: {fruta}")
print(f"Total é R$ {total:.2f}")
print(f"Desconto R$ {valor_desconto:.2f}")
print(f"Total a Pagar R$ {total_a_pagar:.2f}")




