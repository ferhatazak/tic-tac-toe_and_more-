import random
import time


def controler(mini:str,nombre:int,maxi:str)->int:
    """
    Fonction qui compare les bornes d'un nombre avec celui ci pour eviter toute erreur de saisie.
    La fonction demande de resaisir le nombre "nombre" s'il est incorrect
    Entree  :  2 chaine de caractere, entier
    Sortie  : entier
    """
    affichage : str

    if mini!='None' and maxi!='None':
        while nombre<int(mini) or nombre>int(maxi):
            print("Erreur, le nombre doit être compris entre "+mini+" et "+maxi)
            affichage="Entrez un nombre compris entre "+mini+" et "+maxi+" : "
            nombre=int(input(affichage))

    elif maxi=='None' and mini!='None':
        while nombre<int(mini) :
            print("Erreur, le nombre doit être supérieur ou égale à "+mini)
            affichage="Entrez un nombre supérieur ou égale à "+mini+" : "
            nombre=int(input(affichage))

    elif mini=='None' and maxi!='None':
        while nombre>int(maxi) :
            print("Erreur, le nombre doit être inférieur ou égale à "+maxi)
            affichage="Entrez un nombre inférieur ou égale à "+maxi+" : "
            nombre=int(input(affichage))
    return nombre

def reglesalumette():


    """
    Procedure qui affiche les regles du jeu
    Entrer :  rien
    sortie : rien
    """


    print("Bienvenue dans le jeu des allumettes")
    print("Les règles sont simples :")
    print("Il y a deux joueurs, chaque joueur peut à tour de rôle prélever 1, 2 ou 3 allumettes")
    print("le joueur qui prend le dernière allumette a perdu : ")

    
def scorejeu(perdant:int,joueur:list[str])->list[list[str]]:
    """
    Procédure qui definie le gagnant et le perdant
    Entree : entier, liste de chaine de caractere
    Sortie : tableau de tableau de chaine de caractere

    """
    scoregangant:int
    scoreperdant:int
    if perdant==0:
        gagnant=1
    else:
        gagnant=0
    scoregangant=10
    scoreperdant=0
    print(f"Le joueur {joueur[gagnant]} à gagné {scoregangant} pts\nLe joueur {joueur[perdant]} à gagné {scoreperdant} pts")
    return([[str(joueur[gagnant]),str(scoregangant)],[str(joueur[perdant]),str(scoreperdant)]])

def strategiemachine(nballumette : int ) -> int:
    """
    Fonction qui definie la strategie de la machine en fonction du nombre d'allumette
    Entree : un entier, qui correspend au nombre d'allumette
    Sortie : un entier, qui correspond au choix du nombre d'allumette a enlever par la machine
    """
    # la strategie de la machine et la suivante, la machine et gagne obligatoirement a partir qu'il reste 4 allumettes, et que c'est a son tour de jouer. Elle est le plus vulnerable quand c a son tour et qu'il reste 5 allumette. Le but est donc de tout faire pour qu'il reste 4 allumettes ou moins at que ce soit a sont tour.
    choix : int 
    choixmachine = [1,2,3]
    choix = 0 #pour eviter l'erreur " variable is possibly unbound"

    if nballumette == 2 :
        choix = 1
    if nballumette == 3 : 
        choix = 2
    if nballumette == 4 :
        choix = 3
    if nballumette == 5 or nballumette == 6 or nballumette == 10 :
        choix = 1
    if nballumette == 7 :
        choix = 2
    if nballumette == 8:
        choix = 3
    if nballumette == 9 : 
        choix = 2
    if nballumette < 21 and nballumette > 10 :
        choix = random.choice(choixmachine)
    else :
        choix = 1
    return choix

def principalallumettesmvm3()->list[list[str]]: #humain contre humain 

    """
    Fonction qui correspond au programme proncipale du jeu alumettes
    Entrée : rien
    Sortie : chaine de caractere, qui correspond au score.
    """

    nballumettes : int
    nballumettesenlever : int
    joueur1 : str
    tour:int
    joueur2 : str
    allumettes : str
    joueur:list[str]
    perdu : bool
    score:list[list[str]]
    choix_commence : int 
    perdu=False
    nballumettesenlever=0
    tour=0
    nballumettes=20
    perdu=False

    reglesalumette()
    print()

    joueur1=input("Entrez le nom du joueur 1 : ")
    joueur2=input("Entrez le nom du joueur 2 : ")
    joueur=[joueur1,joueur2]
    allumettes=("|"+" ")*nballumettes
    print()
    print("    Qui doit commencer à jouer ? ")
    print("    1  -  joueur 1 ")
    print("    2  -  joueur 2 ")
    choix_commence=int(input("   :   "))
    print("Il reste ---> ",allumettes)
    print()

    while nballumettes!=1 and perdu==False:


        if nballumettes==0:
            perdu=True
            print(None)
            if tour==0:
                tour=1
            else:
                tour=0
        else:
            if choix_commence == 1: 
                print()
                print(joueur1, "est en train de jouer...")
                time.sleep(1) #1 sec de delay 
                nballumettesenlever = strategiemachine(nballumettes)
                nballumettes=nballumettes-nballumettesenlever
                allumettes=("|"+" ")*nballumettes
                print("Il reste ---> ",allumettes)
            choix_commence = 2

            choix_commence =2

            if choix_commence == 2: 
                print()
                print(joueur2, "est en trainde jouer...")
                time.sleep(1) #1 sec de delay 
                choixmachine = [1,2,3] #la machine dispose de trois choix 
                nballumettesenlever = random.choice(choixmachine)
                nballumettes=nballumettes-nballumettesenlever
                allumettes=("|"+" ")*nballumettes
                print("Il reste ---> ",allumettes)
            choix_commence = 1

                
                


    score=scorejeu(tour,joueur) #les tours sont inversé : 0 désigne mtn le joueur2 et 1 désigne mtn le joueur1

    return score

if __name__=="__main__":
    print(principalallumettesmvm3())