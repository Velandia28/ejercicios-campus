datos= {
    "inscritos":{
    "131312": {"nombre":"luis", "edad": 21, "carrera": "ciclismo"},
    "12383":{"nombre":"laura", "edad": 23, "carrera": "patinaje "},
    "452211": {"nombre":"jorge", "edad": 30, "carrera": "atletismo"}
    },
    }

def registrar_inscripcion(data):
        if data["inscritos"].get(años, None)== None:
            if años >= 18 and depar == ("santander"):
                print("**********************")
                inscrito={}
                doc=input("ingrese su documento: ")    
                inscrito["nombre"]=input("ingrese su nombre:  ")
                inscrito["carrera"]=input("a que carrera va a ingresar -atletismo -ciclismo -patinaje : ")
                inscrito["edad"]=input("verifique su edad: ")
                data["inscritos"][doc]=inscrito
            else:
                años<18 and depar!=("santander")
                print("**************************")
                print("no puede inscribirse a ninguna carrera debido a su edad  o departamento de origen !!")
               
while True: 
n    depar=input("Cual es su departamento de origen:  ")
    
    opc_menu = ("1.Para registrar participante","2.salir ")
  
    print("*********************************************************")
    print("Seleccione ->")
    for i in opc_menu:
        print(i)
    opc = int(input("Ingrese la opción deseada: "))
   
    if opc ==len(opc_menu):
        print("Saliendo...")
        break
    elif opc== 0:
         print(datos["inscritos"])
    elif opc == 1:
        registrar_inscripcion(datos)



    