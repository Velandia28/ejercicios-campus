#Escribir un programa que reciba una cadena de caracteres 
# e imprima el tamaño de la cadena, la cadena en mayusculas
# la cadena en minusculas, la cadena invertida y la segunda mitad de la cadena.

frase =input("esciba una frase corta :  ")
print (frase)

longitud=len(frase)
print(longitud)

mayusculas=frase.upper()
print(mayusculas)

minusculas=frase.lower()
print (minusculas)

innver_frase=frase[::-1]
print (innver_frase)

sub_frase=frase.split(",")
print(sub_frase)

        