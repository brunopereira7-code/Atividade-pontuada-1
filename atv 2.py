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
      
        print(f"o seu nome é {nome}")
        print(f"o seu sexo é {sexo}")
        print(f"o seu estado civil é {estado_civil}") 

        if estado_civil == "casada":
            quanto_tempo=input("quantos anos:") 
            print(f"{quanto_tempo} anos")

    case _: 
        print("dados nao achado")


    

    



 




