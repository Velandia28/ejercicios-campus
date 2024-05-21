# Escribir una función que calcule el área de un círculo y
# otra que calcule el volumen de un cilindro usando la primera función.
PI = 3.14
def circulo1 (area):
    circulo =PI*(area**2)
    return  circulo
print("el area del circulo es ", circulo1(2))

def cilindro(altura):
    volumen=(circulo1 *altura)
    return volumen

print("el volumen del cilindro es" ,cilindro)


 