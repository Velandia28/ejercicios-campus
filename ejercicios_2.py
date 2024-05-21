# Escribir una función que calcule el área de un círculo y
# otra que calcule el volumen de un cilindro usando la primera función.
PI = 3.14
area =(float(input("digite el radio el circulo : ")))
def circulo1 (area):
    circulo =PI*(area**2)
    return  circulo 
print(circulo1(area)," es la area del circulo")

altura=(float(input("digite la altura del cilindro : ")))
def cilindro(altura):
    volumen1 =(PI*(area**2)*altura)
    return volumen1
print("el volumen del cilindro es ", cilindro(altura))

 