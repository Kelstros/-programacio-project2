def suma_nombres():
    Primer_Nombre = float (input("Escriu el teu nombre: "))
    Segon_Nombre = float (input("Escriu un altre nombre: "))
    Suma = Primer_Nombre + Segon_Nombre
    print ("La suma dels dos nombres és:", round(Suma))
if __name__ == "__suma_nombres__":
    suma_nombres()