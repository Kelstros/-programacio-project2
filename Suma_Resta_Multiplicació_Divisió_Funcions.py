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
if __name__ == "__calculs_basics__":
    calculs_basics()