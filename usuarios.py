usuario = {'nombre':'' , 'edad' : '' , 'direccion' :'' , 'telefono' : '' }
while True:
    n1= input("ingrese su nombre: ")
    usuario['nombre'] = n1
    e1= input ("ingrese su edad: ")
    usuario['edad'] = e1
    d1= input("ingrese su direccion: ")
    usuario['direccion'] = d1
    t1= input("ingrese su telefono: ")
    usuario['telefono'] = t1
    break


print (usuario)
for valor, llave in usuario.items():
    print (valor, ": ", llave)

print(n1, "tiene", e1, "años.", "vive en ",d1, "y su numero telefonico  es ", t1)