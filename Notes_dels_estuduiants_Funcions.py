def notes_dels_estudiants():
    # Aquesta linia crea la varriable Nombre_de_deus per comptar els 10 introduits
    Nombre_de_deus = 0
    # Aquestes linies demanen a l'usuari que introdueixi les notes
    Nota = int(input("Introdueix una nota entre 0 i 10 (-1 per acabar): "))
    while Nota != -1:
        # Aquesta linia demana una nova nota dintre del bucle
        Nota = int(input("Introdueix una nota entre 0 i 10 (-1 per acabar): "))
        if Nota == 10:
            Nombre_de_deus += 1
        # Aquestes linies comproven si la nota es -1 per aturar el bucle
        if Nota == -1:
            break
    # Aquestes linies comproven si hi ha hagut alguna nota que te un 10
    if Nombre_de_deus == 10:
        print("Hi ha hagut almenys un 10")
    else:
        print("No hi ha cap 10")
if __name__ == "__notes_dels_estudiants__":
    notes_dels_estudiants()