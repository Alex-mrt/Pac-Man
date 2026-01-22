# coding: utf-8
largeur_case=20
hauteur_case=20

from classe_pacman import*
from classe_fantome import*
from ecran import*

menu=False

def afficher_grille(grille,pacman):
    """ 
    Affiche la grille de jeu en fonction des valeurs dans la matrice 'grille'.
    Parcourt chaque cellule de la grille et affiche les éléments associés
    (pastilles, fruits, cases vides) selon leur valeur. Affiche également le score
    et le nombre de vies de Pacman à l'écran. Prends en parametres une grille, et une classe pacman
    """  
    
    petite_pastille=loadImage("bullet-1.png")
    grosse_pastille=loadImage("bullet-2.png")
    
    fruit_cherry=loadImage("fruit-cherry.png")
    fruit_orange=loadImage("fruit-orange.png")
    fruit_strawberry=loadImage("fruit-strawberry.png")
    fruit_apple=loadImage("fruit-apple.png")
    
    case=loadImage("case.png")
                
    for l in range(len(grille)):
        for c in range(len(grille[0])):
            valeur=grille[l][c]
            if valeur==0:
                fill(0,0,0)
                rect((c+0.5)*largeur_case,(l+0.5)*hauteur_case,largeur_case,hauteur_case)
            elif valeur==1:
                image(petite_pastille, (c+0.5)*largeur_case, (l+0.5)*hauteur_case)
            elif valeur==5:
                image(grosse_pastille, (c+0.5)*largeur_case, (l+0.5)*hauteur_case)
            elif valeur==10:
                image(case, (c+0.5)*largeur_case, (l+0.5)*hauteur_case)
            elif valeur==11: #11 est une nouvelle valeur, correspondante aux fruits
                image(fruit_cherry, (c+0.5)*largeur_case, (l+0.5)*hauteur_case)
            elif valeur==12: #12 est une nouvelle valeur, correspondante aux fruits
                image(fruit_strawberry, (c+0.5)*largeur_case, (l+0.5)*hauteur_case)                
            elif valeur==13: #13 est une nouvelle valeur, correspondante aux fruits
                image(fruit_orange, (c+0.5)*largeur_case, (l+0.5)*hauteur_case)        
            elif valeur==14: #14 est une nouvelle valeur, correspondante aux fruits
                image(fruit_apple, (c+0.5)*largeur_case, (l+0.5)*hauteur_case)

                
    
    textSize(25)
    fill (255,255,255)
    text("Score:"+str(pacman.score),700,height/3)
    text("Nombre de vie :"+str(pacman.nbr_vies),700,height/4)

    
        
def verifier_victoire(grille):
    """ 
    Vérifie si le joueur a gagné en vérifiant si toutes les pastilles et fruits ont été mangés.
    Parcourt la grille à la recherche des valeurs correspondant aux objets encore présents 
    (pastilles et fruits). Si l'une de ces valeurs est trouvée, retourne False (victoire non obtenue).
    Si toutes les pastilles et fruits sont mangés, retourne True (victoire obtenue). Prends en parametre une grille et retourne un booleen selon la condition de victoire
    """
    
    for l in range(len(grille)):
        for c in range(len(grille[0])):
            if grille[l][c]==14 or grille[l][c]==13 or grille[l][c]==12 or grille[l][c]==11 or grille[l][c]==5 or grille[l][c]==1:
                return False
    return True
                
def jouer(grille,pacman,fantomes):
    """ 
    Gère une étape du jeu, en affichant la grille, en mettant à jour Pacman et les fantômes.
    Appelle plusieurs méthodes de Pacman et des fantômes pour faire avancer le jeu, changer
    la direction, gérer les collisions et les actions de Pacman (manger des pastilles, activer le
    super mode, etc.). Prends en parametre une grille, une classe pacman et une liste de classe fantomes
    """
    #On lance toutes les methodes associes au jeu
    afficher_grille(grille,pacman)
    pacman.afficher()
    pacman.changer_direction()
    pacman.avancer()
    pacman.est_au_centre()
    pacman.mange_pastille()
    pacman.temps_super_mode()
    for fantome in fantomes:
        fantome.afficher()
        fantome.changer_direction()
        fantome.avancer()
        pacman.collision(fantome)
        pacman.effrayer_fantome(fantome)
    
    
