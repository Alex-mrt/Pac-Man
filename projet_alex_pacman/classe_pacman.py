# coding: utf-8
import time
from math import sqrt

class Pacman:
    def __init__(self,grille):
        """
        Initialisation des attributs de pacman, prends en parametre une grille
        """     
          
        self.img=loadImage("pacman1_START.png")
        self.img_RIGHT_1=loadImage("pacman1_RIGHT.png")     
        self.img_LEFT_1=loadImage("pacman1_LEFT.png")     
        self.img_UP_1=loadImage("pacman1_UP.png")     
        self.img_DOWN_1 =loadImage("pacman1_DOWN.png") 
        self.img_RIGHT_2=loadImage("pacman2_RIGHT.png")     
        self.img_LEFT_2=loadImage("pacman2_LEFT.png")     
        self.img_UP_2=loadImage("pacman2_UP.png")     
        self.img_DOWN_2 =loadImage("pacman2_DOWN.png")         
        
        self.etat="pacman1" #On definit l'etat de pacman
        self.nbr_vies=3
        self.score=0
        self.grille=grille        
        self.x=30
        self.y=30
        self.r=9
        self.direction=None
        self.vitesse=1
        self.duree_super=6
        self.directions=None 
        self.temps_debut=None 
        self.temps_debut_jeux=time.time() #On definit ici le temps, pour connaitre la duree totale du jeu de pacman
        self.duree_jeux=300 #On definit ici le temps totale de jeux
    
    def pacman_reset(self,grille,difficulte):
        """
        Reinitialise Pacman avec ses valeurs de depart.
        """
        
        self.grille=grille
        self.x=30
        self.y=30
        self.direction=None
        self.directions=None
        self.temps_debut=None
        self.temps_debut_jeux=time.time()
        self.score=0
        self.img=loadImage("pacman1_START.png")
        self.etat="pacman1"
        #Selon la difficulte, on redefinira ces valeurs
        if difficulte=="facile":
            self.nbr_vies=5
            self.duree_super=10
        if difficulte=="moyen":
            self.nbr_vies=3
            self.duree_super=7       
        if difficulte=="difficile":
            self.nbr_vies=1
            self.duree_super=5

    def afficher(self):
        """
        Affiche Pacman a sa position actuelle avec son image.
        """
        
        image(self.img,self.x,self.y)

    def changer_direction(self):
        """
        Change la direction de Pacman en fonction de la touche presse.
        """
        
        if keyPressed==True and self.est_au_centre()==True: #Si pacman trouve les bonnes conditions pour pouvoir tourner
            self.vitesse=1
            ancienne_direction=self.direction #on enregistre l'ancienne direction dans le cas ou la nouvelle direction ne serait possible
            self.direction=keyCode
            if self.direction_est_valide()==True: #si la nouvelle direction est possible
                if self.etat=="pacman1": #si pacman est normal
                    if self.direction==RIGHT: 
                        self.img=self.img_RIGHT_1
                        self.directions="RIGHT"  
                    elif self.direction==LEFT:       
                        self.img=self.img_LEFT_1
                        self.directions="LEFT"
                    elif self.direction==DOWN:            
                        self.img=self.img_DOWN_1
                        self.directions="DOWN"       
                    elif self.direction==UP:            
                        self.img=self.img_UP_1
                        self.directions="UP"
                else: #sinon 
                    if self.direction==RIGHT: 
                        self.img=self.img_RIGHT_2
                        self.directions="RIGHT"  
                    elif self.direction==LEFT:       
                        self.img=self.img_LEFT_2
                        self.directions="LEFT"
                    elif self.direction==DOWN:            
                        self.img=self.img_DOWN_2
                        self.directions="DOWN"       
                    elif self.direction==UP:            
                        self.img=self.img_UP_2
                        self.directions="UP"
            else:
                self.direction=ancienne_direction
        
    def avancer(self):
        """
        Fait avancer Pacman dans la direction actuelle si elle est valide.
        """
        
        if self.direction_est_valide()==True:
            if self.direction==RIGHT:  
                self.x+=self.vitesse   
            elif self.direction==LEFT:    
                self.x-=self.vitesse       
            elif self.direction==DOWN:      
                self.y+=self.vitesse         
            elif self.direction==UP:            
                self.y-=self.vitesse
    
    def change_etat(self):
        """
        Change Pacman en super Pacman ('pacman2')
        """
        
        self.etat="pacman2"
        self.img=loadImage("pacman2_"+self.directions+".png") #POUR CHARGER DIRECTEMENT LA TEXTURE DE SUPERPACMAN
        self.temps_debut=time.time() #on definit le temps de debut a 0 en utilisant le module time.time()
    
    def effrayer_fantome(self,fantome):
        """
        Prends en parametre une liste fantome, et declenche la methode effrayer du fantome afin de l'effrayer si pacman est en super mode
        """
        
        if self.etat=="pacman2":
            fantome.change_etat_effrayer() #on appelle la classe fantome pour declencher sa methode effrayer
        else:
            fantome.change_etat_normal()

    def temps_super_mode(self):
        """
        Verifie si Pacman doit revenir en mode normal apres la duree du super mode.
        """
        
        if self.temps_debut!=None: #on verifie si le temps a etait definit
            if time.time()-self.temps_debut>=self.duree_super: #de qu'il atteint 5secondes on retransforme pacman en normal
                self.etat="pacman1"
                self.img=loadImage("pacman1_"+self.directions+".png") #POUR CHARGER DIRECTEMENT LA TEXTURE DE SUPERPACMAN
                self.temps_debut=None
                
    def temps_fin_jeu(self):
        """
        Retourne False ou True selon si la duree du temps de jeu est ecoulee
        """
        
        if self.temps_debut_jeux !=None:  #on verifie si le temps a etait definit
            if time.time() - self.temps_debut_jeux >= self.duree_jeux:  #de qu'il atteint 20secondes on dit que la fonction est True (c'est donc la fin du jeux)
                return True
        return False
    
    def est_au_centre(self):
        """
        Verifie si Pacman est au centre d'une cellule.
        """
        
        if self.x%20==10 and self.y%20==10:
            return True
        else:
            return False    

    def direction_est_valide(self):
        """
        Verifie si la direction actuelle de Pacman est valide.
        """
        
        if self.est_au_centre()==True:
            indice_ligne=self.y//20
            indice_colonne=self.x//20
            if self.direction==RIGHT:
                return self.grille[indice_ligne][indice_colonne + 1]!=10
            elif self.direction == LEFT:
                return self.grille[indice_ligne][indice_colonne - 1]!=10
            elif self.direction == DOWN:
                return self.grille[indice_ligne + 1][indice_colonne] != 10
            elif self.direction == UP:
                return self.grille[indice_ligne - 1][indice_colonne] != 10
        else:
            return True
    
    def mange_pastille(self):
        """
        Viens supprimer l'element qu'a manger pacman de la grille, et ajotue les points associes
        """
        
        if self.est_au_centre()==True:      
            indice_ligne=self.y//20      
            indice_colonne=self.x//20       
            if self.grille[indice_ligne][indice_colonne]==1:          
                self.grille[indice_ligne][indice_colonne]=0 
                self.score+=1 #si pastille simple +1        
            elif self.grille[indice_ligne][indice_colonne]==11: #fruits          
                self.grille[indice_ligne][indice_colonne]=0 
                self.score+=20 #A DECIDER DU SCORE
            elif self.grille[indice_ligne][indice_colonne]==12: #fruits           
                self.grille[indice_ligne][indice_colonne]=0 
                self.score+=20
            elif self.grille[indice_ligne][indice_colonne]==13: #fruits            
                self.grille[indice_ligne][indice_colonne]=0  
                self.score+=20
            elif self.grille[indice_ligne][indice_colonne]==14: #fruits            
                self.grille[indice_ligne][indice_colonne]=0 
                self.score+=20      
            elif self.grille[indice_ligne][indice_colonne]==5:        
                self.grille[indice_ligne][indice_colonne]=0      
                self.score+=5   #si pastille grosse +5
                self.change_etat() # on change pacman en super pacman
    
    def perdre_vie(self):
        """
        Decremente le nombre de vie de Pacman.
        """
        self.nbr_vies=self.nbr_vies-1 #-1 vie
    
    def collision(self,fantome):
        """
        Verifie la collision entre Pacman et un fantome, et gere les consequences.
        """
        
        distance=sqrt((fantome.x-self.x)**2+(fantome.y-self.y)**2)
        if distance<=self.r+fantome.r:
            if self.etat=="pacman1": #si pacman est touche pendant qu'il est normal on renitialise ses coordonees et egalement celle du fantome pour eviter tout bug
                self.x=30
                self.y=30
                fantome.x=330
                fantome.y=210
                self.perdre_vie()
            else: #sinon il tue le fantome et on gagne du score et on renitialise les coordonnes du fantome
                self.score+=50
                fantome.x=330
                fantome.y=210 




    
        
    
    
