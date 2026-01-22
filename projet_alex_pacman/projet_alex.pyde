import csv
from jeu import*
from ecran import*

affichage="accueil"
temps=0
grille1=None
grille2=None
pac_man=None
#fantome=None
fantomes=[]
difficulte=None

def initialiser_grille(nom_fichier):
    """ 
    Charge une grille depuis un fichier CSV spécifié par 'nom_fichier' et retourne une matrice 2D d'entiers représentant la grille du jeu. 
    """

    file = open(nom_fichier , "r") 
    grille=[]
    for ligne in csv.reader(file , delimiter = ",") :
        l=[]
        for n in ligne:
            l.append(int(n))
        grille.append(l)    
    file.close ()
    return grille

def setup():
    """ 
    Configure le jeu en initialisant les grilles (grille1 et grille2), en créant un objet Pacman et une liste de fantômes avec des positions et des couleurs aléatoires. 
    """

    global grille1,grille2,pac_man,fantomes

    size(800,600)
    imageMode(CENTER)
    rectMode(CENTER)
    textAlign(CENTER) 
    grille1=initialiser_grille("grille1.csv")
    grille2=initialiser_grille("grille2.csv")

    pac_man=Pacman(grille1) #CREATION DE PACMAN AU TOUT DEBUT DU JEU
    for i in range(8):
        liste_couleur=["blue","pink","orange","red"] #création d'une liste des couleurs, afin d'en tirer une au hasard
        indice_aleatoire=randint(0,len(liste_couleur)-1)
        fantomes.append(Fantome(grille1,330,210,liste_couleur[indice_aleatoire])) #on ajoute a la liste, un objet fantome, en renseignant ses coordonées, la grille ou il apparait, et sa couleur
    

def draw():
    """ 
    Gère le déroulement du jeu en fonction de l'état actuel ('accueil', 'jeu', 'victoire', 'terminé') : affiche l'écran d'accueil et permet de choisir la difficulté, 
    lance le jeu avec les paramètres de difficulté, gère la victoire ou la défaite de Pacman, et offre l'option de rejouer ou de quitter après la fin du jeu. 
    """

    background(0,0,0)
    global affichage,temps,fantomes,grille1,grille2,difficulte
    if affichage=="accueil":
        choix=accueil() #On viens recupurer la difficulte choisi et la stocker dans une variable afin d'eviter les lags
        if choix=="facile": #Si facile, on redéfinit la vie de pacman et son temps de super, ainsi que la grille choisi
            pac_man.nbr_vies=5
            pac_man.duree_super=10
            difficulte='facile'
            pac_man.grille=grille1 #On modifie la grille qui par défaut est sur grille1
            for fantome in fantomes:
                fantome.grille=grille1
            affichage="jeu"
            print(affichage)
        
        if choix=="moyen": #Si moyen, on redéfinit la vie de pacman et son temps de super
            pac_man.nbr_vies=3
            pac_man.duree_super=7
            difficulte='moyen'
            affichage="jeu"
        
        if choix=="difficile": #Si difficile, on redéfinit la vie de pacman et son temps de super, ainsi que la grille choisi
            pac_man.nbr_vies=1
            pac_man.duree_super=5
            difficulte='difficile'
            pac_man.grille=grille2 #On modifie la grille qui par défaut est sur grille1
            for fantome in fantomes: 
                fantome.grille=grille2
            affichage="jeu"
            

    if pac_man.nbr_vies==0: #si pacman n'a plus de vie, c'est game over
        affichage="terminé"
    
    if verifier_victoire(pac_man.grille): #si pacman a tous manger, c'est la victoire
        affichage="victoire"
    
    if affichage=="jeu": 
        jouer(pac_man.grille,pac_man,fantomes) #On lance le jeu
        if pac_man.temps_fin_jeu():
            affichage="terminé"
    
    if affichage=="victoire":
        if victoire()=="rejouer":
            grille1=initialiser_grille("grille1.csv")
            grille2=initialiser_grille("grille2.csv")
            
            if difficulte=='difficile': #On redefinit donc également dans pacman la grille rénitialiser afin d'afficher la nouvelle
                pac_man.grille=grille2
            if difficulte=='facile':
                pac_man.grille=grille1
            if difficulte=='moyen':
                pac_man.grille=grille1
                
            for fantome in fantomes:
                fantome.fantome_reset()
            pac_man.pacman_reset(pac_man.grille,difficulte)
            affichage="jeu"
    
    if affichage=="terminé":
        if fin()=="rejouer":
            grille1=initialiser_grille("grille1.csv")
            grille2=initialiser_grille("grille2.csv")
            
            if difficulte=='difficile': #On redefinit donc également dans pacman la grille rénitialiser afin d'afficher la nouvelle
                pac_man.grille=grille2
            if difficulte=='facile':
                pac_man.grille=grille1
            if difficulte=='moyen':
                pac_man.grille=grille1
                
            for fantome in fantomes:
                fantome.fantome_reset()
            pac_man.pacman_reset(pac_man.grille,difficulte)
            affichage="jeu"
    
    


            
        
    
