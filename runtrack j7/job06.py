
index_list = []

# Message d'invite
prompt = "\nEntrez une note (ou 'quit' pour finir) : "

while True:
    # Lire la saisie de l'utilisateur
    saisie = input(prompt)

    # Vérifier si l'utilisateur veut quitter
    if saisie.lower() == 'quit':
        break

    try:
        # Convertir la saisie en nombre
        note = float(saisie)
        # Ajouter la note à la liste
        index_list.append(note)
    except ValueError:
        print("Veuillez entrer un nombre valide ou 'quit' pour terminer.")

print("\nVoici la liste des notes :", index_list)

   






# liste_notes = [12,45.48,83,22,35,58,34,41.56]


# for i in liste_notes[0]:
#     if liste_notes < 40:
#         print('vous avez echoué')
#     if liste_notes > 40:
#         print('reussit')
#     if liste_notes > 40:
#         if liste_notes == float :
#             liste_notes += 
#     liste_notes[0] += 1





# def arrondir_notes(liste_notes):
#     notes_arrondies = []
    
#     for note in liste_notes:

#         note = round(note)
        

#         if note < 40:
#             notes_arrondies.append(note)
#             continue
        

#         prochain_multiple = ((note // 5) + 1) * 5
        
#         if (prochain_multiple - note) < 3:
#             note = prochain_multiple
        
#         notes_arrondies.append(note)
    
#     return notes_arrondies


# liste_notes = [12, 45.48, 83, 22, 35, 58, 34, 41.56]
# resultat = arrondir_notes(liste_notes)
# print("Notes originales :", liste_notes)
# print("Notes arrondies  :", resultat)

