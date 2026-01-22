# coding: utf-8
def accueil():
    """ 
    Affiche l'écran d'accueil du jeu avec un fond, un logo et des boutons pour sélectionner le niveau.
    Charge l'image du logo et du fond, puis affiche le texte pour chaque bouton correspondant aux 
    niveaux de difficulté (Facile, Moyen, Difficile). Retourne une chaîne de caractères indiquant le niveau 
    sélectionné (facile, moyen, difficile) si l'utilisateur clique sur un bouton.
    """    
    
    ma_police = createFont("Arcade.ttf", 32)
    image_logo=loadImage("pacman-logo.png")
    image_fond=loadImage("pacman-background.png")

    background(0,0,0)
    image(image_fond, 400, 300, width, height)
    image(image_logo, width / 2 - image_logo.width / 26, height / 4)

    textFont(ma_police)
    fill (255,255,255)
    textSize(32)
    textAlign(CENTER)
    
    if bouton(width/2.2,1.5*height/3,200,60,'Niveau Facile'):
        return "facile"
    if bouton(width/1.8,2*height/3,200,60,'Niveau Moyen'):
        return "moyen"
    if bouton(width/2,2.5*height/3,200,60,'Niveau Difficile'):
        return "difficile"
    


def bouton(x,y,largeur,hauteur,texte):
    """ 
    Crée un bouton interactif à l'écran. Si le curseur de la souris est dans les limites du bouton, 
    celui-ci change de couleur et affiche le texte. Si le bouton est cliqué, retourne True.
    Les paramètres sont la position du bouton (x, y), sa taille (largeur, hauteur), et le texte à afficher.
    Retourne True si le bouton est cliqué, sinon False.
    """
    
    if  x-largeur/2< mouseX < x + largeur/2 and  y - hauteur/2< mouseY < y + hauteur/2 :
        fill (140,90,190)
        rect(x,y,largeur,hauteur,20)
        fill(0,0,0)
        text(texte,x,y+hauteur*0.2)
        if mousePressed :
            return True
    else:
        fill (100,70,170)
        rect(x,y,largeur,hauteur,20)
        fill(0,0,0)
        text(texte,x,y+hauteur*0.2)
    return False

def fin(): 
    """ 
    Affiche l'écran de fin de jeu avec un message "PERDU", un fond et des boutons pour rejouer ou quitter.
    Lorsque l'utilisateur clique sur "Rejouer", retourne "rejouer", sinon si "Quitter" est cliqué, le jeu se ferme.
    """
    global affichage
    image_fond=loadImage("pacman-background.png")
    image(image_fond, 400, 300, width, height)
    textSize(60)
    fill (100,70,170)
    text("PERDU",width/2,height/2.9)
        
    textSize(32)
    if bouton(width/2.2,1.5*height/3,200,60,'Rejouer'):
        return "rejouer"

    if bouton(width/1.8,2*height/3,200,60,'Quitter'):
        exit()

def victoire(): 
    """ 
    Affiche l'écran de victoire avec un message "VICTOIRE", un fond et des boutons pour rejouer ou quitter.
    Lorsque l'utilisateur clique sur "Rejouer", retourne "rejouer", sinon si "Quitter" est cliqué, le jeu se ferme.
    """
    global affichage
    image_fond=loadImage("pacman-background.png")
    image(image_fond, 400, 300, width, height)
    textSize(60)
    fill (100,70,170)
    text("VICTOIRE",width/2,height/2.9)
        
    textSize(32)
    if bouton(width/2.2,1.5*height/3,200,60,'Rejouer'):
        return "rejouer"

    if bouton(width/1.8,2*height/3,200,60,'Quitter'):
        exit()
