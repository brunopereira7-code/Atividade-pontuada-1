import os 
os.system("cls") 

letra_a=int(input("digite seu numero A:"))
letra_b=int(input("digite seu numero B:"))
letra_c=int(input("digite seu numero C:")) 

soma=letra_a+letra_b+letra_c
multiplicacao=letra_a * letra_b

if letra_a == letra_b: 
    soma=letra_a + letra_b
 
print(f"o resultado da soma é {soma}")
print(f"o resultado da multiplicacao é {multiplicacao}")

