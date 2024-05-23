#Escribir un programa que almacene el abecedario en una lista, 
#elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
#y muestre por pantalla la lista resultante.
mates=[]
notas=[]
while True:
    mate=input("que materia esta viendo : ")
    mates.append(mate)
    #print(mates)

    nota=int(input(" digite la nota de la materia : "))
    notas.append(nota)

    if nota>=50:
        mates.pop()
        notas.pop()

        #print(mates)
    elif nota<50 :
        print(mates)
        print(notas)
        print ("debe repertir la materia : ", mates)
        break
    

