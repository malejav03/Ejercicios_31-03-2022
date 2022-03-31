print ("elija una de las sigueintes banderas")
print("carreras, roja, arcoiris y pirata")

paises=input("digite la bandera que escogio:")

if paises== 'carreras' :
    banderas=("U0001F3C1")
    print("\U0001F3C1")
    
elif paises =='roja':
    banderas =("U0001F6A9")
    print("\U0001F6A9")
    
elif paises =='arcoiris':
    banderas =("\U0001F3F3")
    print(banderas)

elif paises =='pirata':
    banderas =("\U0001F3F4")
    print(banderas)
    
else:
    banderas= ' '

print("")