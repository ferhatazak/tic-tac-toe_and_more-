from random import randint
from time import sleep
from time import time

# définir les symbolees pour chaque joueur
player1 = "X"
player2 = "O"

# définir la grille de jeu
#plateau_jeu = ["7", "8", "9","4", "5", "6","1", "2", "3"]
plateau_jeu = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]

# définir les fonctions pour afficher et mettre à jour la grille de jeu
def affichage():
    """Procédure qui affiche le plateau de jeu
    """
    print(plateau_jeu[0] + " | " + plateau_jeu[1] + " | " + plateau_jeu[2])
    print("---------")
    print(plateau_jeu[3] + " | " + plateau_jeu[4] + " | " + plateau_jeu[5])
    print("---------")
    print(plateau_jeu[6] + " | " + plateau_jeu[7] + " | " + plateau_jeu[8])
    print()


# définir la fonction pour vérifier si un joueur a gagné
def finpartie(symbole:str)->bool:
    """Fonction qui vérifie sui la partie est terminée

    Args:
        symbole (str): _description_

    Returns:
        bool: _description_
    """
    fin:bool
    fin=False
    if plateau_jeu[0] == symbole and plateau_jeu[1] == symbole and plateau_jeu[2] == symbole:
        fin=True
    elif plateau_jeu[3] == symbole and plateau_jeu[4] == symbole and plateau_jeu[5] == symbole:
        fin=True
    elif plateau_jeu[6] == symbole and plateau_jeu[7] == symbole and plateau_jeu[8] == symbole:
        fin=True
    elif plateau_jeu[0] == symbole and plateau_jeu[3] == symbole and plateau_jeu[6] == symbole:
        fin=True
    elif plateau_jeu[1] == symbole and plateau_jeu[4] == symbole and plateau_jeu[7] == symbole:
        fin=True
    elif plateau_jeu[2] == symbole and plateau_jeu[5] == symbole and plateau_jeu[8] == symbole:
        fin=True
    elif plateau_jeu[0] == symbole and plateau_jeu[4] == symbole and plateau_jeu[8] == symbole:
        fin=True
    elif plateau_jeu[2] == symbole and plateau_jeu[4] == symbole and plateau_jeu[6] == symbole:
        fin=True
    return fin

# définir la fonction pour vérifier si la grille est pleine
def verif_plein()->bool:
    """Fonction qui vérifie si le plateau est plein

    Returns:
        bool: Vrai si le plateu est plain
    """
    plein:bool
    plein=True
    for i in range(9):
        if plateau_jeu[i] == " ":
            plein=False
    return plein

# définir la fonction pour l'IA pour jouer un coup
def leJeu(symbole:str):
    """Precedure qui joue au morpion en assignant les marque à leurs cases

    Args:
        symbole (str): la marque
    """
    i:int
    j:int
    i=0
    j=0
    nbsav:str
    nbsav=""
    gagner=False
    bloquer=False
    bon=False
    # recherche d'une position pour gagner
    while i!=9 and gagner==False:
        if plateau_jeu[i] != "X" and plateau_jeu[i] != "O":
            nbsav=plateau_jeu[i]
            plateau_jeu[i] = symbole
            if finpartie(symbole) == True and gagner==False:
                gagner=True
                affichage()
            else:
                plateau_jeu[i] = nbsav
        i=i+1
    if gagner==False:
        # recherche d'une position pour bloquer l'adversaire
        while j!=9 and bloquer==False:
            if plateau_jeu[j] != "X" and plateau_jeu[j] != "O":
                nbsav=plateau_jeu[j]
                plateau_jeu[j] = symbole
                if finpartie(symbole) == True and bloquer==False:
                    bloquer=True
                    affichage()  
                else:
                    plateau_jeu[j] = nbsav
            j=j+1
    if bloquer==False and gagner==False:
        # jouer un coup au hasard
        while bon==False:
            n=randint(1,9)
            if plateau_jeu[n-1] == " ":
                plateau_jeu[n-1] = symbole
                bon=True
                affichage()
                


def principale()->list[list[str]]:
    """fonction principale du morpion Machine VS Machine

    Returns:
        list[list[str]]: renvoie le score
    """
    resultat:list[list[str]]
    symbole:str
    tour:int
    fin:bool
    i:int
    joueurgagnant:int#contient le tour du joueur gagnant
    joueur:list[str]
    resultat=[['',''],['','']]
    symbole=player1
    tour=0
    fin=False
    i=1
    joueur=["Machine 1","Machine 2"]
    print("Les machines sont en train de jouer..")
    print()
    while i!=9 and fin==False:
        i=i+1
        leJeu(symbole)
        sleep(1)
        fin=finpartie(symbole)
        #print(fin)
        if tour==0:
           symbole=player2
           tour=1
        else:
            tour=0
            symbole=player1
    if tour==0:#remet le trour dans le bon ordre
        joueurgagnant=1
    else:
        joueurgagnant=0
    resultat=scorepartie(joueur,tour,fin,joueurgagnant,i)
    return(resultat)

def scorepartie(joueur:list[str],tour:int,aligne3marques:bool,joueurgagnant:int,cpt:int)->list[list[str]]:
    """
    Fonction qui attribut les scores
    Entrée : tableau de chaine de caracteres contenant le nom des joueurs,
    la variable "tour" qui est un entier qui correspond à l'indice du joueur perdant dans le tableau,
    la variable "joueurgagnant" qui est un entier qui correspond à l'indice du joueur gagnant dans le tableau,
    un booleen qui indique vrai si la partie est terminé et s'il y a un gagnant ou faux si la partie est fini parce qu'il n'y a plus de case.

    Sortie : tableau de tableau de chaine de caracteres correspondant aux scores
    """
    scoregangant:int
    scoreperdant:int
    scoregangant=0 #pour eviter l'erreur "scoregagnant" is possibly unbound
    scoreperdant=0 #pour eviter l'erreur "scoreperdant" is possibly unbound
    if aligne3marques==False: #signifie égalité
        scoregangant=30
        scoreperdant=30
        print("égalité !")
    else:
        scoregangant=150-(cpt*10)# il faut au minimum 5 coups pour aligner 3 marques (en comptant les coups de l'advesraire)
        scoreperdant=cpt+1
    print("Le joueur ",joueur[joueurgagnant]," à gagné ",scoregangant," pts\nLe joueur ",joueur[tour]," à gagné ",scoreperdant," pts")
    return([[str(joueur[joueurgagnant]),str(scoregangant)],[str(joueur[tour]),str(scoreperdant)]])


        
        
    

  

    print("Voici les temps d'éxecution du modes Stratégique\n",tabStrat,"\nPour une moyenne de ",moyenneStrat)
if __name__ =="__main__":
    print(principale())
   