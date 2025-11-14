def comparar_nombres():
    # A les linies següents es demanen tres nombres
    Nombre1 = input("Introdueix el primer nombre: ")
    Nombre2 = input("Introdueix el segon nombre: ")
    Nombre3 = input("Introdueix el tercer nombre: ")
    # A continuació es comparen els nombres quin és el més gran
    if Nombre1 >= Nombre2:
        if Nombre1 >= Nombre3:
            print("El nombre més gran es:", int(Nombre1))
    if Nombre2 >= Nombre1:
        if Nombre2 >= Nombre3:
            print("El nombre més gran es:", int(Nombre2))
    if Nombre3 >= Nombre1:
        if Nombre3 >= Nombre2:
            print("El nombre més gran es:", int(Nombre3))
if __name__ == "__comparar_nombres__":
    comparar_nombres()