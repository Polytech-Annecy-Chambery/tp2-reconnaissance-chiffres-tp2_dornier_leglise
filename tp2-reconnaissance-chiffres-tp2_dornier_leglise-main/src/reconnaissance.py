from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles




def reconnaissance_chiffre(image, liste_modeles, S):
    #initialisation du compteur de modèles :
    compteur = 0
    #initialisation du maximum de similitude :
    similitude = 0
    #binarisation et localisation de l'image étudiée :
    image_bin = image.binarisation(S)
    image_loc = image_bin.localisation()
    #parcours des modèles :
    for i in range(len(liste_modeles)):
        modele = liste_modeles[i] 
        #redimensionnement de l'image pour la comparaison avec le modèle :
        image = image_loc.resize(modele.H, modele.W)
        temporaire = image.similitude(modele)
        #comparaison de la similitude temporaire avec la similitude max :
        if temporaire > similitude :
            #modification des compteurs et du max de similitude :
            similitude = temporaire 
            compteur = i 
    #renvoi du numéro du modèle        
    return compteur



