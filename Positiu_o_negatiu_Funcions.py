def positiu_negatiu():
    # Ara es demanara un nombre
    Nombre = input("Introdueix un nombre positiu o negatiu: ")
    # Aquestes linies comproven si el nombre es positiu o negatiu
    if int(Nombre) >= 0:
        print("El nombre és positiu.")
    else:
        print("El nombre és negatiu.")
if __name__ == "__positiu_negatiu__":
    positiu_negatiu()