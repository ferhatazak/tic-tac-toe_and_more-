from random import randint
from time import sleep
from strategiehvmavance import *
from morpionMvsM import principale as morpionMvsM

Nbtests:int
Nbtests=10

def reglesmorpion():
    """
    Procedure qui affiche les regles du jeu
    Entrer :  rien
    sortie : rien
    """
    print("Bienvenue dans le jeu du morpion")
    print("Les règles sont simples :")
    print("Chaque joueur pose sa marque (un O ou un X) à tour de role dans les cases d'une grille de 3*3")
    print("Le premier joueur qui aligne 3 marques gagne")
    print("Pour choisir où mettre sa marque")
    print("le jeu vous demandera de saisir le nombre correspondant à l'endroit ou vous souhaitez la placer")

def creematrice(Tailletab:int)->list[list[str]]:
    """
    Fonction qui creer une matrice
    Entree : entier
    Sortie : tableau contenant un tableau de chaine de caractere
    """
    val:str
    i:int
    indice:int
    tabmatrice:list[list[str]]
    ligne:list[str]
    nbval:int
    nbval=Tailletab**2
    tabmatrice=[['']]*Tailletab

    for i in range(Tailletab):
        ligne=['']*Tailletab
        for indice in range (Tailletab,0,-1):
            val=str(nbval)
            nbval=nbval-1
            ligne[indice-1]=val
        tabmatrice[i]=ligne
    return(tabmatrice)

def afficher(matrice:list[list[str]])->str:
    """
    fonction qui affiche un tableau matriciel sous la forme d'une grille de morpion au format d'une chaine de caractere
    Entrée : tableau de tableau contenant une chaine de caracteres
    Sortie : chaine de caractere

    """

    affichage:str
    i:int
    indice:int
    barre=" | "
    affichage=" "
    indice=0 #pour eviter l'erreur: "indice" is possibly unbound
    for i in range(len(matrice)):
        for indice in range(len(matrice[i])-1):
            affichage=affichage+str(matrice[i][indice])+barre
        if i==(len(matrice)-1):
            affichage=affichage+str(matrice[i][indice+1])+"\n"
        else:
            affichage=affichage+str(matrice[i][indice+1])+"\n ---------\n "
    return affichage

def jeu(tabmatrice:list[list[str]],joueur:list[str],tour:int)->list[list[str]]:
    """
    fonction qui permet au joueur de jouer lorsque c'est son tour et lui permet de choisir ou poser sa marque
    Entrée : tableau de tableau de chaine de caractere contenant les nombres et les marques, le tableau contenant le nom des deux joueurs ainsi que le numero correspondant au tour du joueur (l'indice)
    Sortie : tableau de tableau contenant la meme chaine de caractere avec la modification apportée par le joueur
    """
    n:str
    marque:str
    bon:bool
    i:int
    j:int
    bon=False
    marque=''
    if tour==0:
        print("Au joueur "+joueur[tour]+" de poser sa marque : ")
        marque='X'


    elif tour==1:
        print("Au joueur "+joueur[tour]+" de poser sa marque : ")
        marque='O'

    while bon!=True:
        n=input("Entrer le nombre correspondant : ")
        while n=="":
            n=input("Entrer le nombre correspondant : ")
        for i in range(len(tabmatrice)):
            for j in range(len(tabmatrice[i])):
                if n==tabmatrice[i][j] and tabmatrice[i][j]!='X' and tabmatrice[i][j]!='Y':
                    tabmatrice[i][j]=marque
                    bon=True

        if bon==False:
            print("erreur choisisser un autre enplacement, celui ci est déja pris")

    return tabmatrice

def finpartie(tabmatrice:list[list[str]],tour:int,dimension:list[int])->bool:

    """
    Fonction qui verifie la configuration des marques du tableau matriciel et indique si la partie est ou non finie
    Entrée : tableau de tableau de chaine de caractere
    Sortie : booleen
    """
    finjeu:bool
    j:int
    i:int
    ligne:int
    colonne:int
    gagneligne:bool
    gagnecolonne:bool
    gagnediagonale:bool
    marque:str
    gagneligne=False

    ligne=dimension[0]

    colonne=dimension[1]
    gagnecolonne=False
    gagnediagonale=False
    finjeu=False
    if tour==0:
        marque="X"
    else:
        marque="O"

    #Gagner horizontalement
    i=0
    for j in range(0,ligne):
        if tabmatrice[j][i] == marque and tabmatrice[j][i+1] == marque and tabmatrice[j][i+2] == marque :
            gagneligne=True

    # Gagner verticalement
    if gagneligne!=True:
        j=0
        for i in range(colonne):
            if tabmatrice[j][i] == marque and tabmatrice[j+1][i] == marque and tabmatrice[j+2][i] == marque :
                gagnecolonne=True

        #Gagner en diagonale montante depuis en bas a gauche jusqu'à en haut a droite)
        if gagnecolonne!=True:
            i=0
            j=2
            if tabmatrice[j][i] == marque and tabmatrice[j-1][i+1] == marque and tabmatrice[j-2][i+2] == marque:
                gagnediagonale=True
            #Gagner en diagonale descendante (depuis en haut a gauche jusqu'à en bas a droite)
            if gagnediagonale!=True:
                j=0
                i=0
                if tabmatrice[j][i] == marque and tabmatrice[j+1][i+1] == marque and tabmatrice[j+2][i+2] == marque :
                    gagnediagonale=True
    if  gagneligne==True or gagnecolonne==True or gagnediagonale==True:
        finjeu=True
    return finjeu

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
    else:
        scoregangant=150-(cpt*10)# il faut au minimum 5 coups pour aligner 3 marques (en comptant les coups de l'advesraire)
        scoreperdant=cpt+1
    print("Le joueur ",joueur[joueurgagnant]," à gagné ",scoregangant," pts\nLe joueur ",joueur[tour]," à gagné ",scoreperdant," pts")
    return([[str(joueur[joueurgagnant]),str(scoregangant)],[str(joueur[tour]),str(scoreperdant)]])

def principalmorpion(joueur:list[str])->list[list[str]]:
    """
    Fonction qui correspond au programme principale du jeu morpion
    Entrée : rien
    Sortie : tableau de tableau de chaine de caractere qui correspond au score
    """
    Tailletab:int
    tour:int
    joueurgagnant:int
    matrice:list[list[str]]
    aligne3marques:bool #vrai si un joueur aligne 3 marques
    score:list[list[str]]
    cpt:int
    aligne3marques=False
    tour=0
    cpt=0
    Tailletab=3
    reglesmorpion()
    print()
    matrice=creematrice(Tailletab)
    while aligne3marques!=True and cpt!=Tailletab**2:
        print (afficher(matrice))
        matrice=jeu(matrice,joueur,tour)
        aligne3marques=finpartie(matrice,tour,[Tailletab,Tailletab])
        print()
        if tour==1:
            tour=0
        elif tour==0:
            tour=1
        cpt=cpt+1

    if tour==1:
        joueurgagnant=0
    else:
        joueurgagnant=1
    if aligne3marques==True:
        print()
        print (afficher(matrice))
        print("vous avez gagné",joueur[joueurgagnant])
        score=scorepartie(joueur,tour,aligne3marques,joueurgagnant,cpt)
    else:
        print()
        print (afficher(matrice))
        print("égalité ! la partie est finie")
        score=scorepartie(joueur,tour,aligne3marques,joueurgagnant,cpt)
    return(score)

def meunuchoixdesmodesdejeux():
    print("Bienvenue dans le menu du choix des jeux")
    print("1 - jouer humain contre humain")
    print("2 - jouer humain contre machine")
    print("3 - jouer machine contre machine\n")

def choixdesjeuxmorpion()-> list[list[str]]:
    saisie:int
    resultat:list[list[str]]
    joueur1:str
    joueur2:str
    joueur:list[str]
    strategie:int
    saisie=0
    resultat=[[""],[""]] # pour éviter l'erreur "resultat" is possibly unbound
    meunuchoixdesmodesdejeux()
    while saisie<1 or saisie>3:
        saisie=int(input("Entrez le nombre : "))
    if saisie==1:
        joueur1=input("Entrez votre nom joueur 1 : ")
        joueur2=input("Entrez votre nom joueur 2 : ")
        joueur=[joueur1,joueur2]
        resultat=principalmorpion(joueur)
    if saisie==2:

        strategie=choixStrategie()
        #stratégie=1 -> mode aléatoire
        #stratégie=2 -> mode stratégique
        if strategie == 1 : 
            humainMachine=choisirquicommence()
            #humainMachine=1 -> humain commence
            #humainMachine=2 -> machine commence
            if humainMachine==1:
                joueur1=input("Entrez votre nom de joueur : ")
                joueur2="Machine"
                joueur=[joueur1,joueur2]
                resultat=principalmorpionhumainMachine(joueur,strategie)
            else:
                joueur1="Machine"
                joueur2=input("Entrez votre nom de joueur : ")
                joueur=[joueur1,joueur2]
                resultat=principalmorpionhumainMachine(joueur,strategie)
        if strategie == 2 : 
            principalehvmstrat()
       
    if saisie==3:
        
        joueur=["Machine 1","Machine 2"]
        strategie=choixStrategie()
        if strategie == 1 : 
            resultat=principalmorpionMachineMachine(joueur,strategie)
        if strategie == 2 : 
            resultat=morpionMvsM()

    return resultat

def menuchoisirquicommence():
    print("Ce menu permet de décider qui commence")
    print("1 - L'humain commence")
    print("2 - La machine commence\n")

def choisirquicommence():
    saisie:int
    saisie=0
    menuchoisirquicommence()
    while saisie<1 or saisie>2:
        saisie=int(input("Entrez le nombre : "))
    return saisie


def menuChoixStrategie():
    print("Bienvenue dans le menu du choix des strategies")
    print("1 - mode aléatoire")
    print("2 - mode stratégique\n")

def choixStrategie():
    saisie:int
    saisie=0
    menuChoixStrategie()
    while saisie<1 or saisie>2:
        saisie=int(input("Entrez le nombre : "))
    return saisie

def principalmorpionhumainMachine(joueur:list[str],strategie:int)->list[list[str]]:
    """
    Fonction qui correspond au programme principale du jeu morpion
    Entrée : rien
    Sortie : tableau de tableau de chaine de caractere qui correspond au score
    """
    Tailletab:int
    tour:int
    joueurgagnant:int
    matrice:list[list[str]]
    aligne3marques:bool #vrai si un joueur aligne 3 marques
    score:list[list[str]]
    cpt:int
    aligne3marques=False
    tour=0
    cpt=0
    Tailletab=3
    reglesmorpion()
    print()
    matrice=creematrice(Tailletab)
    while aligne3marques!=True and cpt!=Tailletab**2:
        print (afficher(matrice))
        if strategie==1:
            matrice=jeuhumainmachineAlea(matrice,joueur,tour)#jeu aleatoire
        #else:
        #    matrice=jeuhumainmachineStra(matrice,joueur,tour)#jeu stratégique

        aligne3marques=finpartie(matrice,tour,[Tailletab,Tailletab])
        print()
        if tour==1:
            tour=0
        elif tour==0:
            tour=1
        cpt=cpt+1

    if tour==1:
        joueurgagnant=0
    else:
        joueurgagnant=1
    if aligne3marques==True:
        print()
        print (afficher(matrice))
        print("vous avez gagné",joueur[joueurgagnant])
        score=scorepartie(joueur,tour,aligne3marques,joueurgagnant,cpt)
    else:
        print()
        print (afficher(matrice))
        print("égalité ! la partie est finie")
        score=scorepartie(joueur,tour,aligne3marques,joueurgagnant,cpt)
    return(score)

def jeuhumainmachineAlea(tabmatrice:list[list[str]],joueur:list[str],tour:int)->list[list[str]]:
    """
    fonction qui permet au joueur de jouer lorsque c'est son tour et lui permet de choisir ou poser sa marque
    Entrée : tableau de tableau de chaine de caractere contenant les nombres et les marques, le tableau contenant le nom des deux joueurs ainsi que le numero correspondant au tour du joueur (l'indice)
    Sortie : tableau de tableau contenant la meme chaine de caractere avec la modification apportée par le joueur
    """
    n:str
    marque:str
    bon:bool
    i:int
    j:int
    bon=False
    marque=''
    if tour==0:
        print("Au joueur "+joueur[tour]+" de poser sa marque : ")
        marque='X'
    elif tour==1:
        print("Au joueur "+joueur[tour]+" de poser sa marque : ")
        marque='O'
    while bon!=True:
        if (tour==0 and joueur[tour]=="Machine" ) or (tour==1 and joueur[tour]=="Machine"):
            n=Machinealeatoire()
        else:
            n=input("Entrer le nombre correspondant : ")
            while n=="":
                n=input("Entrer le nombre correspondant : ")

        for i in range(len(tabmatrice)):
            for j in range(len(tabmatrice[i])):
                if n==tabmatrice[i][j] and tabmatrice[i][j]!='X' and tabmatrice[i][j]!='Y':
                    tabmatrice[i][j]=marque
                    bon=True
        if bon==False:
            print("erreur choisisser un autre emplacement, celui ci est déja pris")
    return tabmatrice

def principalmorpionMachineMachine(joueur:list[str],strategie:int)->list[list[str]]:
    """
    Fonction qui correspond au programme principale du jeu morpion
    Entrée : rien
    Sortie : tableau de tableau de chaine de caractere qui correspond au score
    """
    Tailletab:int
    tour:int
    joueurgagnant:int
    matrice:list[list[str]]
    aligne3marques:bool #vrai si un joueur aligne 3 marques
    score:list[list[str]]
    cpt:int
    aligne3marques=False
    tour=0
    cpt=0
    Tailletab=3
    reglesmorpion()
    print()
    matrice=creematrice(Tailletab)
    while aligne3marques!=True and cpt!=Tailletab**2:
        print (afficher(matrice))
        if strategie==1:
            matrice=jeuMachinemachineAlea(matrice,joueur,tour)#jeu aleatoire
        aligne3marques=finpartie(matrice,tour,[Tailletab,Tailletab])
        print()
        if tour==1:
            tour=0
        elif tour==0:
            tour=1
        cpt=cpt+1

    if tour==1:
        joueurgagnant=0
    else:
        joueurgagnant=1
    if aligne3marques==True:
        print()
        print (afficher(matrice))
        print("vous avez gagné",joueur[joueurgagnant])
        score=scorepartie(joueur,tour,aligne3marques,joueurgagnant,cpt)
    else:
        print()
        print (afficher(matrice))
        print("égalité ! la partie est finie")
        score=scorepartie(joueur,tour,aligne3marques,joueurgagnant,cpt)
    return(score)

def jeuMachinemachineAlea(tabmatrice:list[list[str]],joueur:list[str],tour:int)->list[list[str]]:
    """
    fonction qui permet au joueur de jouer lorsque c'est son tour et lui permet de choisir ou poser sa marque
    Entrée : tableau de tableau de chaine de caractere contenant les nombres et les marques, le tableau contenant 
    le nom des deux joueurs ainsi que le numero correspondant au tour du joueur (l'indice)
    Sortie : tableau de tableau contenant la meme chaine de caractere avec la modification apportée par le joueur
    """
    n:str
    marque:str
    bon:bool
    i:int
    j:int
    bon=False
    marque=''
    if tour==0:
        print("Au joueur "+joueur[tour]+" de poser sa marque : ")
        marque='X'
    elif tour==1:
        print("Au joueur "+joueur[tour]+" de poser sa marque : ")
        marque='O'
    while bon!=True:
        if (tour==0 and joueur[tour]=="Machine" ) or (tour==1 and joueur[tour]=="Machine"):
            n=Machinealeatoire()
            sleep(0.5)
        else:
            n=str(randint(1,9))
            sleep(0.5)
        for i in range(len(tabmatrice)):
            for j in range(len(tabmatrice[i])):
                if n==tabmatrice[i][j] and tabmatrice[i][j]!='X' and tabmatrice[i][j]!='Y':
                    tabmatrice[i][j]=marque
                    bon=True
    return tabmatrice

def Machinealeatoire():
    n:str
    n=str(randint(1,9))
    return n




if __name__=="__main__":
    
    print(choixdesjeuxmorpion())
    
    

