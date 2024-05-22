# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla.

asignaturas=[]
while  True:
    mns=(input("que materias ve en el instituto : "))
    if mns == "":
        print("el ejercio ha finalizado ")
        break
    else :
        asignaturas.append(mns)
    print (asignaturas)
        
