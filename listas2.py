# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista 
# y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> 
# es cada una de las asignaturas de la lista.


materia=[]

nombre=(input("escriba su nombre :  "))
while True:
    input("para finalizar deje vacio el campo siguiente ")    
    msn=input("que asignaturas ve en el curso :")
    if msn=="":
         print("el ejercio ha finalizado ")
         break
    materia.append(msn)
print ("yo  estudio ",materia)

    
