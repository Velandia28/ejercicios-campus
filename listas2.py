# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista 
# y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> 
# es cada una de las asignaturas de la lista.


materia=[]

nombre=(input("escriba su nombre :  "))
while True:
    print("para finalizar escriba 0 en el siguiente campo ")    
    msn=input("que asignaturas ve en el curso :")
    #materia.append(msn)
    #print ("yo  estudio ",materia)
    if msn=="0":
         print("el ejercio ha finalizado ")
         break
    materia.append(msn)
print ("yo  estudio ",materia)

    
