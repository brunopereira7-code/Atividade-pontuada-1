import os 
os.system("cls") 

print("""
Fruta\tAté 5 Kg\tAcima de 5 Kg
Morango-R$ 2,50 por Kg	R$ 2,20 por Kg
Maçã-   R$ 1,80 por Kg	R$ 1,50 por Kg
      """)

fruta=input("qual frutas voce quer:").lower()
quantidade=float(input("quantas vc quer:"))


preco_por_kg= 0


match fruta .strip().lower():
    case "morango":
        if quantidade <=5:
            preco_por_kg=2.50

        else:
            preco_por_kg=2.20

    case "maça": 
        if quantidade <= 5:
            preco_por_kg=1.80

        else:
            preco_por_kg=1.50

    case _:
        print("dados invalidos")
         
if  preco_por_kg> 0:
    total_a_pagar = quantidade * preco_por_kg
            
print(f"a sua fruta é {fruta}")
print(f"a sua quantidadeé {quantidade}")
print(f"o preco por kg é {preco_por_kg:.2f}")
print(f"o Total  é {total_a_pagar:.2f}")





