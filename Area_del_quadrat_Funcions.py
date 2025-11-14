def area_del_quadrat():
    # Aquesta linia pregunta la mida del costat d'un quadrat
    print ("Anem a calcular l'àrea d'un quadrat, introdueix la mida d'un costat")
    # En aquestes linies, es llegeix la mida del costat introduida per l'usuari i calcula l'area
    costat = int(input ("Mida del costat: "))
    àrea = costat * costat
    # per acabar, es mostra l'àrea del quadrat a la pantalla
    print ("l'àrea del cuadrat es:", int(àrea))
if __name__ == "__area_del_quadrat__":
    area_del_quadrat()