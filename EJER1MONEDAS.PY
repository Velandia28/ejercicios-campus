#1. Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al 
#usuario por una divisa y muestre su símbolo o un 
#mensaje de aviso si la divisa no está en el diccionario.
dinero = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = (input("ingrese una divisa: "))
for valor in dinero :
    if divisa == "euro":
        print (dinero['Euro'])
        break
    elif divisa == "dolar":
        print (dinero['Dollar'])
        break
    elif divisa == "yen":
        print(dinero['Yen'])
        break
    elif divisa != dinero:
        print ("divisa no encontrada")  
        break