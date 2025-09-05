import os 
os.system("cls") 

letra_a=float(input("digite suas letras A:"))
letra_b=float(input("digite suas letras B:"))
letra_c=float(input("digite a letra C:"))

soma= letra_a + letra_b

if letra_a and letra_b< letra_c: 
    print("é menor que letra  c")

elif letra_a and letra_b> letra_c: 
    print("é maior que letra c")

else:
    ("letra errada digite de novo")

print(f"a soma do numero a e b é {soma}")



