# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
#Si el divisor es cero el programa debe mostrar un error.

num_1 =int(input("digite el primer numero para la division  "))
num_2 =int(input(" digite el segundo numero para la division  "))

if num_2 > 0 :
    print (num_1/num_2)
 
elif num_2 == 0 :
    print ("error no se puede dividir en 0  ")