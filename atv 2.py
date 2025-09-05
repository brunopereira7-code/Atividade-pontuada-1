import os 
os.system("cls")

nome=input("Digite seu nome:")
sexo=input("Digite seu sexo:")
estado_civil=input("digite seu estado civil:") 

match sexo:
    
    case "masculino":  

        print(f"o seu nome é {nome}")
        print(f"o seu sexo é {sexo}")
        print(f"o seu estado civil é {estado_civil}")

     
 
    case "feminino":
         
        if estado_civil=="casada":
         quanto=int(input("digite o tempo de casada:"))

      
        print(f"o seu nome é {nome}")
        print(f"o seu sexo é {sexo}")
        print(f"o seu estado civil é {estado_civil}") 
        print(f"o seu tempo de casada é {quanto} anos") 

    case _: 
        print(f"o seu nome é {nome}")
        print(f"o seu sexo é {sexo}")
        print(f"o seu estado civil é {estado_civil}")


    

    



 




