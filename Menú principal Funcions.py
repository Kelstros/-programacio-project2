def HolaMundo():
    print("Hola, Mundo!")
def area_del_quadrat():
    costat = float(input("Introdueix la longitud del costat del quadrat: "))
    area = costat * costat
    print(f"L'àrea del quadrat és: {area}")
def suma_nombres():
    num1 = float(input("Introdueix el primer nombre: "))
    num2 = float(input("Introdueix el segon nombre: "))
    suma = num1 + num2
    print(f"La suma dels nombres és: {suma}")
def frase_feta():
    frase = input("Introdueix una frase feta: ")
    print(f"La frase feta és: {frase}")
def major_o_menor():
    edat = int(input("Introdueix la teva edat: "))
    if edat >= 18:
        print("Ets major d'edat.")
    else:
        print("Ets menor d'edat.")
def nombres_parells():
    print("Nombres parells de 1 a 200:")
    for num in range(2, 201, 2):
        print(num, end=' ')
    print()
def notes_estudiants():
    num_estudiants = int(input("Introdueix el nombre d'estudiants: "))
    notes = []
    for _ in range(num_estudiants):
        nota = float(input("Introdueix la nota de l'estudiant: "))
        notes.append(nota)
    print("Notes dels estudiants:", notes)
def positiu_o_negatiu():
    Nombre = input("Introdueix un nombre positiu o negatiu: ")
    if float(Nombre) > 0:
        print("El nombre és positiu.")
    elif float(Nombre) < 0:
        print("El nombre és negatiu.")
    else:
        print("El nombre és zero.")
def positiu_negatiu():
    Nombre = input("Introdueix un nombre positiu o negatiu: ")
    if float(Nombre) > 0:
        print("El nombre és positiu.")
    elif float(Nombre) < 0:
        print("El nombre és negatiu.")
    else:
        print("El nombre és zero.")
def positiu_o_negatiu_llista():
    llista_nombres = [10, -5, 0, 23, -1, 7]
    for nombre in llista_nombres:
        if nombre > 0:
            print(f"{nombre} és positiu.")
        elif nombre < 0:
            print(f"{nombre} és negatiu.")
        else:
            print(f"{nombre} és zero.")
def quin_nombre_mes_gran():
    num1 = float(input("Introdueix el primer nombre: "))
    num2 = float(input("Introdueix el segon nombre: "))
    if num1 > num2:
        print(f"{num1} és més gran que {num2}.")
    elif num2 > num1:
        print(f"{num2} és més gran que {num1}.")
    else:
        print("Els dos nombres són iguals.")
def calculs_basics():
    # Aquesta linia "imprimeix" el que fara el programa
    print ("Anem a sumar, restar, multiplicar i dividir dos nombres")
    # En aquestes linies, es llegeix els dos nombres introduits per l'usuari i realitza les operacions
    nombre1 = int(input ("Introdueix el primer nombre: "))
    nombre2 = int(input ("Introdueix el segon nombre: "))
    # Ara es realitzen les operacions i s'emmagatzemen en variables
    suma = nombre1 +nombre2
    resta = nombre1 - nombre2
    multiplicació = nombre1 * nombre2
    divisió = nombre1 / nombre2
    # Finalment, es mostren els resultats per pantalla
    print ("la suma es:", int(suma), "la resta es:", int(resta), "la multiplicació es:", int(multiplicació), "la divisió es:", divisió)
while True:
    print("1. Hello, World!")
    print("2. Àrea del quadrat")
    print("3. Casting nombres")
    print("4. Frase feta")
    print("5. Major o menor d'edat")
    print("6. Nombres parells de 1 a 200")
    print("7. Notes dels estudiants")
    print("8. Positiu o negatiu")
    print("9. Positiu o negatiu en la llista")
    print("a. Quin nombre és més gran?")
    print("b. Suma, Resta, Multiplicació, Divisió")
    print("S. Sortir")
    opcio = input("Que desitjes fer? ")
    match opcio:
        case "1":
            HolaMundo()
        case "2":
            area_del_quadrat()
        case "3":
            suma_nombres()
        case "4":
            frase_feta()
        case "5":
            major_o_menor()
        case "6":
            nombres_parells()
        case "7":
            notes_estudiants()
        case "8":
            positiu_negatiu()
        case "9":
            positiu_o_negatiu()
        case "a":
            quin_nombre_mes_gran()
        case "b":
            calculs_basics()
        case "S" | "s":
            print("Fins aviat!")
            break
        case _:
            print("Opció no vàlida. Si us plau, intenta-ho de nou.")

