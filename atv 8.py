import os 
os.system("cls") 

print(""" 
    Cor	Preço
Verde	R$ 10,00
Azul	R$ 20,00
Amarelo	R$ 30,00
Vermelho R$ 40,00

      """) 
cor=input("Digite sua cor:")

match cor .strip().lower():
    case"verde":
        print("Cor:verde\npreço:R$ 10,00")
    case"azul":
        print("Cor:Azul\npreço R$ 20,00")

    case"amarelo":
        print("Cor:Amarelo\npreço R$ 30,00")

    case"vermelho":
        print("Cor:Vermelho\npreço R$ 40,00")

    case _:
        print("Dados incorretos")
    
print("\tBoas compras!")



        
 