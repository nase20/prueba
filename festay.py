baraja={}
def agregar_carta(cartas:dict, codigo: str, datos: list)->bool:
    if codigo not in cartas:
        cartas [codigo]= {"nivel":datos[0], "energia": datos[1]}
        return True
    return False
def usar_carta(cartas:dict, codigo: str, gasto: int)->bool:
    if codigo in cartas:
        datos=cartas[codigo]
        if gasto<=(datos[cartas][energia]):
            cartas[codigo]={"nivel":[0]}
            return True
        print("nivel *")
        return False
def listar_cartas(cartas):
    print(cartas)
def umbral_bajo(cartas:dict, umbral:int):
    datos=cartas.items(cartas)
    if (datos[cartas])<umbral:
        print(cartas)
while True:
    print("********DECK*******")
    print("")
    print("")
    print("1.- registrar una carta")
    print("2.- usar una carta en batalla")
    print("3.- listar todas las cartas")
    print("4.- mostrar cartas con baja energia")
    print("5.- salir")
    try:
        opcion=int(input("seleccione una opcion: "))
        if opcion==1:
            codigo=input("ingrese codigo de la carta: ")
            energia=int(input("ingrese energia de la carta: "))
            agregar_carta(baraja,codigo, ["",energia])
        elif opcion==2:
            codig=input("ingrese codigo de la carta: ")
            gastar=int(input("ingrese consumo de energia: "))
            if usar_carta(baraja,codig,gastar):
                print("nivel *")
            else:
                print("no es posible incrementar el nivel ")   
        elif opcion==3:
            listar_cartas(baraja)
        elif opcion==4:
            umbral_bajo(baraja,500)
        elif opcion==5:
            break
    except:
        print("seleccione una opcion valida.")