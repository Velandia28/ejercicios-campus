verduras={"brocoli":2500, "pimenton":1250,"arvejas": 3500}
verdu=("brocoli:2500, pimenton : 1250, arvejas 3500./n si desea finalizar escriba ""salir")
print(verdu)
while True:
    verdura=input("que verdura desea comprar? ")
    if verdura=="salir":
        print("gracias por preferirnos, vuelva pronto")
        break
    elif verdura=="brocoli":
        cant=int(input("cuantos kilos desea llevar ? "))
        print(cant*verduras["brocoli"])
    elif verdura=="pimenton":
        cant=int(input("cuantos kilos desea llevar ? "))
        print(cant*verduras["pimenton"])
    elif verdura=="arvejas":
        cant=int(input("cuantos kilos desea llevar ? "))
        print(cant*verduras["arvejas"])
    else:
        print("la verdura no esta disponible")
        
    
