# datos de tipo booleano 
caminante_1 = True  #dato booleano positivo 
caminante_2 = False #dato booleano negativo 
print (caminante_1) #muestra el resultado positivo luego de invoca a la funcion caminante_1

# declaro constantes 
pi=3.1415 #se le asigna un valor a la variable pi
gravedad=9.8  #se le asigan un valor a la variable gravedad
print (pi) #imprime la constante pi
print (gravedad) #imprime la constante gravedad

# de tipo tipado 
time=1.9        # variable de tipo float 
print (type(time)) #imprime el tipo de variable adoptada segun el dato asignado 
 # de tipo int 
times = int(time)   #inivoca la variable anterior de tipo entero
print(times)    #muestra la parte entera asignada a la variable
# de tipo cadena 
primera_cadena= "cadena de hierro " # a la variable se le asigna un mensaje 
print (type (primera_cadena)) # muestra que la cadena es de tipo str
print (primera_cadena) # muestra el mensaje almacenado en la variable pirmera_cadena 
primera_cadena ='cadena de hierro cambia pero \' es de cobre'
print (primera_cadena) #imprime el mensaje pero muestra la segunda comilla sencilla como texto en lugar de delimitador
 # formateo, asigan un valor a cada variable u y la f en la cadena les asigna un formato para el mensaje y mostrar asi los valores de las variables
num_a=5 # se le asigna un valor a la variable
num_b=9 # se le asigna un valor a la variable
mi_seg_cadena= f"los numeros son {num_a} y {num_b}" # se les da formato a las variables con la "f" antes del mensaje y las variables separadas por llaves 
print (mi_seg_cadena) #imprime el mensaje segun el formato asignado 
 # operaciones comunes
cad_1="hola"
cad_2="mundo"
res= cad_1+ " " +cad_2 #suma las dos variables 
print(res) # muestra el resultado de la suma de las dos variables en este caso de tipo str
# longitud de una cadena 
mens ="bucaramanga"
longitud=len(mens) #cuenta el numero de caracteres de la cadena y los guarda dentro de esta variable 
print(longitud) #muestra el numero de caracteres del mensaje de la primer variable 

#acceso a caracteres individuales
fen="Soatá" # se le asigna un mensaje 
primer_caracter=fen[4]  #toma la posicion que determine el usuario partiendo desde 0 
print (primer_caracter) #muestra la letra el mensaje deacuerdo a la posicion que determina el usuario 

#subcadena de una cadena
fen = "soata es lindo" #escribe el mensaje dentro de la variable fen
sub_fen=fen[6:9] # toma los datos de fen y selecciona desde la posicion 6 a la 9 partiendo desde 0 
print(sub_fen) # muestrra el resultado de las letra que estan desde la posicion 6 a la 9 

# busqueda en una cadena
fen="esto es una prueba de busqueda" # variable con mensaje inicial
indice = fen.find("prueba")
nuevo_fen= fen.replace("prueba" ,"PRUEBAai") # nueva variable con funcion de remplazar "prueba" por "PRUEBAa" o el mensaje de las segundas comillas
print(indice) #muestra la palabra que esta indicada dentro del find
print(nuevo_fen) #muestra el mensaje inicial pero remplaza la palabra del indice por la de la nueva sub cadena en este caso "nuevo_fen" con la funcion de remplazar

# conversion de texto mayus a minus
cad="hola mundo " #mensaje a modificar
mayus=cad.upper() # mensaje convertido a mayusculas
minus=cad.lower() #mensaje convertido a minusculas
primer_mayus=cad.capitalize() #mensaje con la primer letra en mayuscula
titulada=cad.title() # mensaje con las primeras letra de cada palabra en mayuscula
print(cad) #imprime el mensaje de la variable sin modificar
print(mayus) # imprime el mensaje convertido a mayusculas
print(minus)# imprime el mensaje convertido en minusculas
print(primer_mayus)#imprime el mensaje con la primer letra del mensaje en mayuscula
print(titulada) #imprime el mensaje con la primer letra de cada palabra en mayuscula
