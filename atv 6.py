import os 
os.system("cls")

nota_1=int(input("digite seu n1:"))
nota_2=int(input("digite seu n2:"))
nota_3=int(input("digite seu n3:"))

soma=nota_1+nota_2+nota_3
divisao=nota_1+nota_2+nota_3
media= nota_1+nota_2/3 

if media >=6:
    print("Aprovado")

elif media <6:
    print("Reprovado")

print(f"o resultado da soma é {soma}")
print(f"o resultado da divisao é {divisao}")
print(f"resultado da media é {media}")

print("Ate logo")