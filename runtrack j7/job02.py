
hauteur = int(input("Entrez la hauteur du triangle : "))


for i in range(hauteur):
    espaces = " " * (hauteur - i - 1)
    gauche = "/"
    interieur = "_" * (2 * i) if i == hauteur - 1 else " " * (2 * i)
    droite = "\\"
    print(espaces + gauche + interieur + droite)

