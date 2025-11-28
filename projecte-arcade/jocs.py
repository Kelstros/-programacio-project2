import random
import robot 

def determinar_guanyador_ronda (jugador, maquina):

    if jugador == maquina:
        return "empat"
    
    # Regles
    if (jugador == "pedra" and maquina == "tisora") or \
       (jugador == "paper" and maquina == "pedra") or \
       (jugador == "tisora" and maquina == "paper"):
        return "jugador"
    
    else:
        return "maquina"

#Joc 1: Pedra, Paper, Tisora
def janken ():

    print("Pedra, Paper, Tisora")

    maquina_joc = robot.robot () 
    
    # 1. Triar joc
    while True:

        mode = input("(1: Primer a 3, 2: Millor de 5): ")

        if mode == '1':
            victories_max, rondes_max = 3, float ('inf')
            break

        elif mode == '2':
            victories_max, rondes_max = float ('inf'), 5
            break

        print("no vàlid.")

    puntuacio_jugador = 0
    puntuacio_maquina = 0
    ronda_actual = 0
    opcions_valides = ["pedra", "paper", "tisora"]

    # Bucle principal del joc
    while puntuacio_jugador < victories_max and puntuacio_maquina < victories_max and ronda_actual < rondes_max:
        ronda_actual += 1

        print(f"Ronda {ronda_actual} ({puntuacio_jugador}-{puntuacio_maquina})")
        
        # 2. Gestió d'entrada de l'usuari
        while True:
            jugada_usuari = input("La teva jugada (pedra/paper/tisora): ")

            if jugada_usuari in opcions_valides:
                break

            print("Jugada no vàlida.")
            
        jugada_maquina = maquina_joc.playing () 
        print(f"Robot: {jugada_maquina}")

        # 3. Comparar/actualitzar puntuacions
        guanyador = determinar_guanyador_ronda (jugada_usuari, jugada_maquina)
        
        if guanyador == "jugador":
            puntuacio_jugador += 1
            print("ronda guanyada.")

        elif guanyador == "maquina":
            puntuacio_maquina += 1
            print("El robot ha guanyat la ronda.")

        else:
            print("Empat.")
            
    # resultat final
    print("Fi")
    
    if puntuacio_jugador == puntuacio_maquina:
        missatge = "empat."

    elif puntuacio_jugador > puntuacio_maquina:
        missatge = f"Has guanyat ({puntuacio_jugador}-{puntuacio_maquina})"

    else:
        missatge = f"El robot guanya la partida ({puntuacio_jugador}-{puntuacio_maquina})"
    
    print(missatge)


#Joc 2: Endevinar Número
def nana ():
    
    print("Endevina el Número")
    print("un número entre l'1 i el 100.")
    numero_secret = random.randint (1, 100)
    intents = 0
    
    while True:
        intent = input("Introdueix número ('s' per sortir): ")
        
        if intent.upper () == 's':
            print("Finalitzat")
            break
        
        try:
            numero_introduit = int (intent)

        except ValueError:
            print("Introducció invalida.")
            
            continue
        
        intents += 1
        
        if numero_introduit < numero_secret:
            print("Més alt.")

        elif numero_introduit > numero_secret:
            print("Més baix.")

        else:
            print(f"correcte: {numero_secret} en {intents} intents.")
            break