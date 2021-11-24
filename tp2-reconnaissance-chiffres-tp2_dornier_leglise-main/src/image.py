from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================



    def binarisation(self, S):
        #création d'une image aux dimensions voulues :
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype = np.uint8))
        #parcours de chaque pixel par ligne et par colonne :
        for i in range(self.H):
            for j in range(self.W):
                #choix de l'action à effectuer pour chaque pixel :
                if self.pixels[i][j] >= S:
                    im_bin.pixels[i][j] = 255 
                else : 
                    im_bin.pixels[i][j] = 0
        #renvoi de l'image binarisée :
        return (im_bin)



    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================



    def localisation(self):  
        #initialisation des curseurs :                               
        c_max = 0
        c_min = self.W
        l_max = 0
        l_min = self.H
        #parcours de chaque pixel de l'image  :
        for l in range(self.H):
            for c in range(self.W):
                #encadrement par les curseurs :
                if self.pixels[l][c] == 0 :
                    if c < c_min :
                        c_min = c
                    elif c > c_max :
                        c_max = c
                    if l < l_min : 
                        l_min = l
                    elif l > l_max :
                        l_max = l
        nb_c = c_max - c_min
        nb_l = l_max - l_min
        #création d'une nouvelle image aux dimensions voulues :
        image = Image()
        image.set_pixels(np.zeros((nb_l, nb_c), dtype = np.uint8))
        #remplacement des pixels de la nouvelle image par les pixels voulus :
        for l in range(nb_l):
            for c in range(nb_c):
                image.pixels[l][c] = self.pixels[l_min+l][c_min+c]
        #renvoi de l'image correctement recadrée :
        return (image)



        
    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================



    def resize(self, new_H, new_W):
        #création d'une image :
        image = Image()
        #variable temporaire avec l'image aux dimensions souhaitées :
        temporaire = resize(self.pixels, (new_H, new_W), 0)
        #conversion de la variable temporaire en tableau d'entiers :
        image.set_pixels(np.uint8(temporaire*255))
        #renvoi de l'image :
        return image
 
    
 
    
    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================




    def similitude(self, im):
        #initialisation du compteur de nombre de pixels identiques :
        compteur = 0
        #parcours de l'image :
        for i in range (self.H):
            for j in range(self.W):
                #comparaison de chaque pixel et modification du compteur :
                if self.pixels[i][j] == im.pixels[i][j]:
                    compteur += 1
        #calcul et renvoi de la similitude :
        similitude = compteur/(self.H*self.W)
        return similitude
    
