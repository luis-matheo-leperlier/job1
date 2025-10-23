
h = int(input("Entrez une valeur pour la hauteur : "))
l = int(input("Entrez une valeur pour la largeur : "))

i = 0

def draw_rectangle(l, h):
    for i in range(h):
        if i == 0 or i == h - 1:
            print('|',"-" * l,'|')
        else:
            print("|" + " " * (l+2) + "|")

draw_rectangle(l, h)
