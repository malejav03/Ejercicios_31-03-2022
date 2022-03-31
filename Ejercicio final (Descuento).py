import random
valor_compra=int(input("Ingrese el monto de su compra: "))
balota =['roja', 'verde', 'blanca', 'verde', 'amarilla']

des_verde=valor_compra-(valor_compra*0.5)
des_blanca=valor_compra-(valor_compra*0.3)
des_negra=valor_compra-(valor_compra*0.2)
des_amarilla=valor_compra-(valor_compra*0.1)

des2_verde=valor_compra*0.5
des2_blanca=valor_compra*0.3
des2_negra=valor_compra*0.2
des2_amarilla=valor_compra*0.1

def selectRandom(balota):
    return random.choice(balota)
colorbalota=selectRandom(balota)
print(f'Su balota es: {colorbalota} ')

if valor_compra > 50000:
     if colorbalota =="rojo":
          print(f'Tines un descuento del 100% eso es {valor_compra} no pagaras nada')
     elif colorbalota =="verde":
          print(f'Tienes un descuento del 50% es {des2_verde}, pagaras {des_verde}')       
     elif colorbalota =="blanca":
          print(f'Tienes un descuento del 30% es {des2_blanca}, pagaras{des_blanca}')
     elif colorbalota =="negra":
          print(f'Tienes un descuento del 20% es {des2_negra}, pagaras {des_negra}')
     elif colorbalota =="amarilla":
          print(f'Tienes un descuento del 10% es {des2_amarilla}, pagaras {des_amarilla}')
else:
     print(f'No Aplica descuento')
