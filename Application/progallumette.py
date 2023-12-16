from allumetteshvh import *
from allumettesale import *
from allumettesnv2 import *
from allumettemvm2 import *
from allumettemvm1 import *
from allumettemvm3 import *
from allumettemvm4 import *

def principaleallumette()->list[list[str]]:
    choix_mode : int 
    choix_difficulte : int 
    resultat:list[list[str]]
    resultat=[[""],[""]]
    affichermode()
    #commande nettoyer le terminal 
    choix_mode = int(input("Choisissez le mode de jeux : "))
    
    while choix_mode < 1 or choix_mode > 3 :
        choix_mode = int(input("Choisissez le mode de jeux existant : "))
    print()

    if choix_mode == 1: #humain contre humain
        resultat=principalallumetteshvh()
    
    if choix_mode == 2:  #humain contre machine 
        choix_difficulte = choixdifficulte()
        if choix_difficulte == 1:
            resultat=principalallumettesaleatoire()
        if choix_difficulte == 2 :
            print(principalallumettesnv2())

    if choix_mode == 3:  #machine contre machine 
        choix_difficulte = choixdifficultemvm()
        if choix_difficulte == 1:
            resultat=principalallumettesmvm1()
        if choix_difficulte == 2 :
            resultat=principalallumettesmvm()
        if choix_difficulte == 3 :
            resultat=principalallumettesmvm3()
        if choix_difficulte == 4 : 
            resultat=principalallumettesmvm4()
    return resultat
if __name__=="__main__":
    print(principaleallumette())