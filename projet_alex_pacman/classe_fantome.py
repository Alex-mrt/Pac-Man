# coding: utf-8
from random import*

class Fantome:
    def __init__(self,grille,x,y,couleur):
        """
        Initialisation des attributs du fantome, prends en parametre une grille, une position x et y, et une couleur
        """   
          
        self.couleur=couleur
        self.img=loadImage("ghost-"+self.couleur+".png")
        self.img_normal=loadImage("ghost-"+self.couleur+".png") #On charge ici l'image normale
        self.img_effrayer=loadImage("ghost-crazy.png") #et l'image effraye
        directions=["UP","DOWN","RIGHT","LEFT"]
        self.direction = directions[randint(0,2)]
        self.grille=grille
        self.x=x
        self.y=y
        self.r=9
        self.vitesse=1
    
    def fantome_reset(self):
        """
        Reinitialise la position du fantome aux coordonnees de depart (330, 210).
        """
        self.x=330
        self.y=210
        
    def afficher(self):
        """
        Affiche l'image actuelle du fantome a sa position (x, y).
        """
        
        image(self.img,self.x,self.y)
    
    
    def directions_possibles(self):
        """
        Retourne la liste des directions possibles (UP, DOWN, LEFT, RIGHT) 
        ou le fantome peut se deplacer en fonction de sa position dans la grille.
        """
        
        liste_direction_possible=[]
        if self.est_au_centre()==True:
            indice_ligne=self.y//20
            indice_colonne=self.x//20
            #On verifie chaque case adjacentes afin de verifier leur etat, si c'est un mur
            if self.grille[indice_ligne][indice_colonne+1]!=10:
                liste_direction_possible.append("RIGHT")
            if self.grille[indice_ligne][indice_colonne-1]!=10:
                liste_direction_possible.append("LEFT")
            if self.grille[indice_ligne-1][indice_colonne]!=10:
                liste_direction_possible.append("UP")
            if self.grille[indice_ligne+1][indice_colonne]!=10:
                liste_direction_possible.append("DOWN")
            return liste_direction_possible
                
    def direction_contraire(self):
        """
        Retourne la direction opposee a la direction actuelle du fantome.
        """
        
        if self.direction=="RIGHT":
            return "LEFT"
        elif self.direction=="LEFT":
            return "RIGHT"
        elif self.direction=="DOWN":
            return "UP"
        elif self.direction=="UP":
            return "DOWN"                
         
 
    def change_etat_effrayer(self):
        """
        Change l'image du fantome pour l'etat effraye.
        """
        self.img=self.img_effrayer
    
    def change_etat_normal(self):
        """
        Remet l'image du fantome a son etat normal.
        """
        
        self.img=self.img_normal

    def avancer(self):
        """
        Met a jour la position du fantome dans la direction actuelle en fonction de sa vitesse.
        """
        
        if self.direction=="RIGHT":  
            self.x+=self.vitesse   
        elif self.direction=="LEFT":    
            self.x-=self.vitesse       
        elif self.direction=="DOWN":      
            self.y+=self.vitesse         
        elif self.direction=="UP":            
            self.y-=self.vitesse

    def est_au_centre(self):
        """
        Verifie si le fantome est au centre de la cellule
        """
        
        if self.x%20==10 and self.y%20==10:
            return True
        else:
            return False    
        
    def direction_aleatoire(self):
        """
        Met a jour l'argument direction selon plusieurs facteurs, on vient chosir une direction aleatoire dans celle possible, et on vient ajouter une chance que le fantome fasse 
        demi tour a l'aide de la methode direction_contraire
        """
        if self.est_au_centre()==True:
            nv_directions=self.directions_possibles() #on definit la liste de directions possible pour sauvegarder les modifications si on devait retirer la direction contraire
            if len(self.directions_possibles())==1:
                self.direction=nv_directions[0]
            else:
                direction_contraire=self.direction_contraire()
                choix=randint(1,100)
                if choix<5and direction_contraire in nv_directions:  # 5% de chance d'aller dans la direction contraire
                    self.direction=direction_contraire
                else:
                    if direction_contraire in nv_directions:
                        nv_directions.remove(direction_contraire)
                        d_aleatoire=randint(0,len(nv_directions)-1)
                        self.direction=nv_directions[d_aleatoire]
    
    def changer_direction(self):
        """
        Change la direction du fantome si celui-ci est au centre ou si la direction est nulle.
        """
        
        if self.est_au_centre()==True or self.direction==None:
            self.direction_aleatoire()
