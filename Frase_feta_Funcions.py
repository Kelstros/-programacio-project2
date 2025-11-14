def frase_feta():
    #Aquesta linia et demana que introdueixis tres paraules
    print ("farem una frase feta amb 3 paraules que ens donis")
    # En aquestes linies, es llegeixen les tres paraules introduides per l'usuari
    paraula1 = input ("Introdueix la primera paraula: ")
    paraula2 = input ("Introdueix la segona paraula: ")
    paraula3 = input ("Introdueix la tercera paraula: ")
    # Tot seguit, es creara una frase feta amb totes les paraules
    frase_feta = "Comprar 1 " + paraula1 + " més 2 " + paraula2 + " i 3 " + paraula3
    # Finalment, es mostra la frase feta per pantalla
    print ("La frase feta es:", frase_feta)
if __name__ == "__frase_feta__":
    frase_feta()