edad= int(input("Introduzca su edad: "))
peso=int(input("Introduzca su peso: "))
pulso=int(input("Introduzca su pulso: "))
plaquetas=int(input("Introduzca sus plaquetas: "))

if edad >= 18  <= 65:
    if peso >= 55:
        if pulso >= 50  <= 110:
            if plaquetas >= 150.000:
                print("Apto para donar sangre")
            else:
                print("No apto para donar sangre") 
        else:
            print("No apto para donar sangre")     
    else:
        print("No apto para donar sangre")             
else:
    print("No apto para donar sangre")
