def major_o_menor():
    # Aquesta linia pregunta la teva edat
    edat = input ("Quants anys tens? ")
    # Aquesta linia condiciona la resposta segons l'edat
    if edat >= 18:
        # Aquesta linia et diu que ets major d'edat si tens 18 anys o més
        print ("Ets major d'edat")
    elif edat < 1:
        print ("Introdueix una edat vàlida")
    # Aquesta linia tracta el cas contrari
    else:
        print ("Ets menor d'edat")
if __name__ == "__major_o_menor__":
    major_o_menor()