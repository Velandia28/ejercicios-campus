def eliminar_participante(data):
    print("**************************************************")
    doc = input("Ingrese el documento: ")
    participante = data["participantes"].get(doc, None)
    if participante != None and participante["Pago"] == False:
        data["participantes"].pop(doc)
        print("Eliminación existosa!")
    else:
        print("Participante no existe o ya pago!")
    print("**************************************************")
