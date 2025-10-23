# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# alphabet2 = []
# mot_cache = input("entrer votre message codé :")
# nombre_de_decalage = int(input("entrer le nombre de decalage :"))
# direction = input("choissisez entre droite et gauche :")


# def nv_alphabet():
#     n = 0
#     for i in range(26):
#         n += 1
#         if direction == 'droite':
#             o = alphabet(nombre_de_decalage,alphabet[n])
#             alphabet2.insert(o)
#         else :
#             o = alphabet(-nombre_de_decalage,alphabet[n])
#             alphabet2.insert(o)



# u = len(mot_cache)

# def mot_dechifre():
#     for u in mot_cache():
#         alphabet == alphabet2

# mot_dechifre()
# print(mot_cache)




alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z']

mot_cache = input("Entrez votre message : ")
nombre_de_decalage = int(input("Entrez le nombre de décalage : "))
direction = input("Choisissez entre 'droite' et 'gauche' : ")


if direction == "gauche":
    nombre_de_decalage = -nombre_de_decalage

def code_cesar(texte, decalage):
    resultat = ""
    for lettre in texte:
        if lettre in alphabet:

            position = alphabet.index(lettre)

            nouvelle_pos = (position + decalage) % 26
            resultat += alphabet[nouvelle_pos]
        else:
            resultat += lettre
    return resultat

mot_code = code_cesar(mot_cache, nombre_de_decalage)
print("Message codé:", mot_code)







    





        

