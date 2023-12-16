from random import randint
from time import sleep
from time import time
Limite:int
Nbtests:int#pour les tests de temps
Nbtests=10
Limite=500 

def reglesdevinette():
    """
    Procedure qui affiche les regles du jeu
    Entrer :  rien 
    sortie : rien
    """
    print("Bienvenue dans le jeu devinette")
    print("Les règles sont simples:")
    print("Ensuite, le joueur numéro 1 entre secrètement le nombre que le joueur numéro 2 doit deviner")
    print("Le joueur numéro 2 doit entrer des nombres jusqu'à ce qu'il trouve le bon : le programme indique si le nombre entré est trop grand ou trop petit.")
    print("Le score maximal du chercheur est de 100 et diminue de 5 à chaque tentative")
    print("Pour finir, le score minimale du joueur 1 est de 0 et augmente de 5 à chaque tentative du joueur 2")

def Score(essai :int,joueur1:str,joueur2:str)->list[list[str]]:
    """
    fonction qui definie les scores 
    Entree : entier, liste de chaine de caractere 
    Sortie : tableau de tableau de chaine de caractere qui corespond au score
    """
    scorej1:int
    scorej2 : int
    scorej2=100
    scorej2=scorej2-(5*(essai-1))
    scorej1=0
    scorej1=scorej1+(5*(essai-1))
    return ([[str(joueur1),str(scorej1)],[str(joueur2),str(scorej2)]])

def principaldevinetteHumainHumain()->list[list[str]]:
    """
    Fonction qui correspond au programme principale du jeu devinette
    Entrée : rien
    Sortie : tableau de tableau de chaine de caractere qui corespond au score finale
    """
    essai : int
    tentative : int #nombre entré par le joueur
    score : list[list[str]]
    joueur1 : str
    joueur2 : str
    affichage : str
    nombreadeviner:int
    message:str
    message=""
    #---------------------------------------------------------------
    
    nombreadeviner=-1 #idem
    tentative=-1 #idem
    #---------------------------------------------------------------
    reglesdevinette()
    print()
    joueur1=input("Entrez votre nom joueur 1 : ")
    joueur2=saisirNom("Entrez votre nom joueur 2 : ")
    print()
    print("La limite de l'intervale de nombre est conpris entre 0 et ",Limite)
    print()
    essai=0
    print("La limite de l'intervale de nombre est ",Limite)
    affichage=str(joueur1)+" saisissez un nombre à deviner : "
    while nombreadeviner<0 or nombreadeviner>Limite:
        try:
            nombreadeviner=int(input(affichage))
        except:
            print("Erreur, il faut entrer un nombre\n")
    print("Le nombre à deviner est "+str(nombreadeviner))
    print(("\n")*100)#saute des lignes pour cacher le nombre a deviner
    print("La limite de l'intervale de nombre est ",Limite)
    while message!="C'est gagner !":
        affichage=str(joueur2)+" saisissez un nombre : "
        tentative=saisirNombre(affichage)
        affichage=str(joueur1)+" saisissez 1 pour trop petit, 2 pour trop grand et 0 pour c'est gagné : "
        message=joueurendefence(tentative,affichage)
        print(message)
        essai=essai+1
    #calcule des scores et enregistrement dans un fichier
    score=Score(essai,joueur1,joueur2)
    print(f"Le joueur {score[1][0]} à gagné {score[1][1]} pts\nLe joueur {score[0][0]} à gagné {score[0][1]} pts")
    return (score)

def menuprincipale():
    """
    Procédure qui affiche le menu du choix des modes de jeu à l'écran
    ENTREE : Rien
    SORTIE : Rien
    """
    print("\nBienvenue dans le menu des devinettes")
    print("(Les precisions sur le modes de jeux seront demandées au fur et à mesure)")
    print("1 - jouer humain contre humain")
    print("2 - jouer humain contre machine")
    print("3 - jouer machine contre machine\n")
    
def menuHumainMachine():
    """
    Procédure qui affiche le menu du choix d'attaque/défense à l'écran
    ENTREE : Rien
    SORTIE : Rien
    """
    print("\nSelectionez le mode de jeu correspondant")
    print("1 - machine qui cherche ")
    print("2 - machine qui envoie le message\n")
    
def choixjeuHumainMachine()->list[list[str]]:
    """
    Fonction qui permet de choisir si la machine attaque ou défend
    ENTREE : Rien
    SORTIE : tableau de tableau de chaine de caractere qui corespond au score finale
    """
    saisie:int
    result:list[list[str]]
    saisie=0
    result=[[""],[""]] #pour éviter le message "valRetour" is possibly unbound
    menuHumainMachine()
    while saisie<1 or saisie>2: #vérifie que le nombre est correct
        try:
            saisie=int(input("\nEntrer le nombre correspondant à l'action que vous souhaitez faire : "))
        except:
            print("Erreur, il faut entrer un nombre\n")
    if saisie==2:
        result=humainenattaque()#il n'y a pas de stratégie pour une machine qui défend
    else:
        result=choixstrategie(saisie,"humainVSmachine")
    return result

def menuchoixstrategie():
    """
    Procédure qui affiche le menu du choix de la stratégie de la machine à l'écran (aléatoire/stratégique)
    ENTREE : Rien
    SORTIE : Rien
    """
    print("\nSaisissez le niveau de la machine")
    print("1 - mode aléatoire")
    print("2 - mode stratégique\n")
    
def choixstrategie(attaquedefence:int,modejeu:str)->list[list[str]]:
    """
    Fonction qui permet de choisir la stratégie de jeu de la machine en attaque
    ENTREE : Rien
    SORTIE : tableau de tableau de chaine de caractere qui corespond au score finale
    """
    #attaquedefence=1 -> la machine attaque
    #attaquedefence=2 -> la machine défend
    saisie:int #stratégie
    resultat:list[list[str]]
    saisie=0
    resultat=[[""],[""]] # pour éviter le message ""resultat" is possibly unbound"
    menuchoixstrategie()
    while saisie<1 or saisie>2: #vérifie que le nombre est correct
        try:
            saisie=int(input("\nEntrer le nombre correspondant à l'action que vous souhaitez faire : "))
        except:
            print("Erreur, il faut entrer un nombre\n")
    #saisie à 1 = attaque aléatoire
    #saisie à 2 = attaque stratégique
    
    if modejeu=="humainVSmachine" and attaquedefence==1 and saisie==1:
        resultat=machineAttaquealeatoire()
    if modejeu=="humainVSmachine" and attaquedefence==1 and saisie==2:
        resultat=machineenattaquestrategique()

        
    if modejeu=="machineVSmachine" and saisie==1: #aléatoire
        resultat=machineContreMachineAttaqueAleatoire()
    if modejeu=="machineVSmachine" and saisie==2: #stratgique
        resultat=machineContreMachineAttaqueStrategique()
    return resultat
    
def choixmodejeu()->list[list[str]]:
    """
    Fonction qui permet de lancer le mode de jeu souhaité
    ENTREE : Rien
    SORTIE : tableau de tableau de chaine de caractere qui corespond au score finale
    """
    saisie:int
    valRetour:list[list[str]]
    saisie=0
    valRetour=[[""],[""]] #pour éviter le message "valRetour" is possibly unbound
    menuprincipale()
    while saisie<1 or saisie>4: #vérifie que le nombre est correct
        try:
            saisie=int(input("\nEntrer le nombre correspondant à l'action que vous souhaitez faire : "))
        except:
            print("Erreur, il faut entrer un nombre\n")
    if saisie==1:
        valRetour=principaldevinetteHumainHumain()
    if saisie==2:
        #principaldevinetteHumainMachine():
        valRetour=choixjeuHumainMachine()
    if saisie==3:
        valRetour=choixstrategie(1,"machineVSmachine")
    return valRetour

def machineAttaquealeatoire():
    """
    Fonction qui correspond au programme principale du jeu devinette machine en mode aléotoire contre humain
    Entrée : rien
    Sortie : tableau de tableau de chaine de caractere qui corespond au score finale
    """
    message:str
    essai : int
    tentative : int #nombre entré par le joueur
    score : list[list[str]]
    joueur1 : str
    joueur2 : str
    affichage : str
    intervmax:int
    intervmin:int
    nombreadeviner:int
    nombreadeviner=-1#initialisation, cette valeur ne correspond a rien
    message=""
    reglesdevinette()
    print()
    joueur1=input("Entrez votre nom joueur qui envoie le message : ") #défence
    joueur2="Machine"                                      #attaque
    print()
    print("La limite de l'intervale de nombre est conpris entre 0 et ",Limite)
    print()
    essai=0
    print("La limite de l'intervale de nombre est ",Limite)
    affichage=str(joueur1)+" saisissez un nombre à deviner : "
    while nombreadeviner<0 or nombreadeviner>Limite:
        try:
            nombreadeviner=int(input(affichage))
        except:
            print("Erreur, il faut entrer un nombre\n")
    print("Le nombre à deviner est "+str(nombreadeviner))

    print(("\n")*100)#saute des lignes pour cacher le nombre a deviner
    print("La limite de l'intervale de nombre est ",Limite)
    intervmin=0
    intervmax=Limite
    while message!="C'est gagner !":
        tentative=randint(intervmin,intervmax)
        affichage=str(joueur1)+" saisissez 1 pour trop petit, 2 pour trop grand et 0 pour c'est gagné : "
        message=joueurendefence(tentative,affichage)
        print(message)
        if message=="Trop petit !":
            intervmin=tentative
        else:
            intervmax=tentative
        essai=essai+1 
    #calcule des scores et enregistrement dans un fichier
    score=Score(essai,joueur1,joueur2)
    print(f"Le joueur {score[1][0]} à gagné {score[1][1]} pts\nLe joueur {score[0][0]} à gagné {score[0][1]} pts")
    return (score)

def joueurendefence(nombre:int,affichage:str)->str:
    """fonction qui demande a l'humain de déterminer si le nombre saisie par la machine est exacte, trop grand ou trop petit

    Args:
        nombre (int): nombre saisie par la machine
        affichage (str):message à afficher a l'écran

    Returns:
        str: message à envoyer à la machine
    """
    indication:int
    message:str
    indication=-1
    print("La machine a entré ",nombre)
    print(affichage)
    while indication<0 or indication>2: #vérifie que le nombre est correct
        try:
            indication=int(input("\nSaisie : "))
        except:
            print("Erreur, il faut entrer un nombre\n")
    if indication==2:
        message="Trop grand !"
    elif indication==1:
        message="Trop petit !"
    else:
        message="C'est gagner !"
    return message
      
def machineendefence(indication:int,val:int)->str:
    """fonction qui demande à la machine de déterminer si le nombre saisie par la machine est exacte, trop grand ou trop petit

    Args:
        indication (int): nombre saisie par la machine
        val (int): nombre à trouver

    Returns:
        str: message à envoyer à la machine
    """
    message:str
    print("Le nombre entré est ",indication)
 
    if indication>val:
        message="Trop grand !"
    elif indication<val:
        message="Trop petit !"
    else:
        message="C'est gagner !"
    return message

def machinegenerernombrealeatoire(min:int,max:int)->int:
    """Fonction qui génère un nombre aléatiore compris entre min et max

    Args:
        min (int): borne minimum
        max (int): borne maximum

    Returns:
        int: Renvoie un entier
    """
    nb:int
    nb=randint(min,max)
    return nb

def humainenattaque()->list[list[str]]:
    """
    Fonction qui correspond au programme principale du jeu devinette humain contre machine
    Entrée : rien
    Sortie : tableau de tableau de chaine de caractere qui corespond au score finale
    """
    indication : int
    essai : int
    score : list[list[str]]
    joueur1 : str
    joueur2 : str
    affichage : str
    nombreadeviner:int
    message:str
    message=""
    indication=-1#initialasation cette valeur ne correspond a rien
    reglesdevinette()
    print()
    joueur1="Machine"                                      #défence 
    joueur2=input("Entrez votre nom joueur qui cherche : ") #attaque
    
    print()
    print("La limite de l'intervale de nombre est conpris entre 0 et ",Limite)
    print()
    essai=0
    print("La limite de l'intervale de nombre est ",Limite)

    nombreadeviner=machinegenerernombrealeatoire(0,Limite)
    print("Le nombre à deviner est "+str(nombreadeviner))

    print(("\n")*100)#saute des lignes pour cacher le nombre a deviner
    print("La limite de l'intervale de nombre est ",Limite)
    affichage=str(joueur2)+" saisissez le nombre à deviner : "
    while message!="C'est gagner !":
        indication=saisirNombre(affichage)
        message=machineendefence(indication,nombreadeviner)
        print(message)
        essai=essai+1
    #calcule des scores et enregistrement dans un fichier
    score=Score(essai,joueur1,joueur2)
    print(f"Le joueur {score[1][0]} à gagné {score[1][1]} pts\nLe joueur {score[0][0]} à gagné {score[0][1]} pts")
    return (score)

def machineenattaquestrategique():
    """
    Fonction qui correspond au programme principale du jeu devinette machine en mode stratégique contre humain et qui fonctionne grace à une recherche dicotomique
    Entrée : rien
    Sortie : tableau de tableau de chaine de caractere qui corespond au score finale
    """
    message:str
    essai : int
    tentative : int #nombre entré par le joueur
    score : list[list[str]]
    joueur1 : str
    joueur2 : str
    affichage : str
    nombreadeviner:int
    tab:list[int]
    nombreadeviner=-1
    message=""
    reglesdevinette()
    print()
    joueur1=input("Entrez votre nom joueur qui envoie le message : ") #défence
    joueur2="Machine"                                      #attaque
    print()
    print("La limite de l'intervale de nombre est conpris entre 0 et ",Limite)
    print()
    essai=0
    print("La limite de l'intervale de nombre est ",Limite)
    affichage=str(joueur1)+" saisissez le nombre à deviner : "
    try:
        nombreadeviner=saisirNombre(affichage)
    except:
        print("Erreur, il faut entrer un nombre\n")
    print("Le nombre à deviner est "+str(nombreadeviner))

    print(("\n")*100)#saute des lignes pour cacher le nombre a deviner
    print("La limite de l'intervale de nombre est ",Limite)
    tab=[0]*(Limite+1)
    for i in range(Limite+1):
        tab[i]=i
    #------------début dichotomie---------------------
    debutTab=0
    finTab=Limite+1 # indice n°501
    while message!="C'est gagner !":
        tentative=(debutTab+finTab)//2
        affichage=str(joueur1)+" saisissez 1 pour trop petit, 2 pour trop grand et 0 pour c'est gagné : "
        message=joueurendefence(tentative,affichage)
        print(message)
        if message=="Trop petit !":
            debutTab=tentative+1
        else:
            finTab=tentative-1
        essai=essai+1 
    #-----------Fin de dichotomie---------------------
    
    #calcule des scores et enregistrement dans un fichier
    score=Score(essai,joueur1,joueur2)
    print(f"Le joueur {score[1][0]} à gagné {score[1][1]} pts\nLe joueur {score[0][0]} à gagné {score[0][1]} pts")
    return (score)

def saisirNombre(affichage:str)->int:
    """Fonction qui demande à l'utilisateur d'entres un nombre compris entre 0 et la limite max prédéfinie
    Args:
        affichage (str): message à afficher à l'écran
        
    Returns:
        int: nombre entier
    """
    saisie:int
    saisie=-1
    print("\n"+affichage)
    while saisie<0 or saisie>Limite: #vérifie que le nombre est correct
        try:
            saisie=int(input("Saisie : "))
        except:
            print("Erreur, il faut entrer un nombre\n")
        return saisie
    
def machineContreMachineAttaqueStrategique():
    """
    Fonction qui correspond au programme principale du jeu devinette machine en mode stratégique
    contre humain et qui fonctionne grace à une recherche dicotomique
    Entrée : rien
    Sortie : tableau de tableau de chaine de caractere qui correspond au score finale
    """
    message:str
    essai : int
    tentative : int #nombre entré par le joueur
    score : list[list[str]]
    joueur1 : str
    joueur2 : str
    nombreadeviner:int
    tab:list[int]
    nombreadeviner=-1
    message=""
    reglesdevinette()
    print()
    joueur2="Machine chercheur" #attaque
    joueur1="Machine message" #défence
    print()
    print("La limite de l'intervale de nombre est conpris entre 0 et ",Limite)
    print()
    essai=0
    print("La limite de l'intervale de nombre est ",Limite)
    print(str(joueur2)+" saisissez un nombre à deviner : ")
    try:
        nombreadeviner=machinegenerernombrealeatoire(0,Limite)
    except:
        print("Erreur, il faut entrer un nombre\n")
    print("Le nombre à deviner est "+str(nombreadeviner))

    print(("\n")*100)#saute des lignes pour cacher le nombre a deviner
    print("La limite de l'intervale de nombre est ",Limite)
    tab=[0]*(Limite+1)
    for i in range(Limite+1):
        tab[i]=i
    #------------début dichotomie---------------------
    debutTab=0
    finTab=Limite+1 # indice n°501
    while message!="C'est gagner !":
        tentative=(debutTab+finTab)//2
        sleep(1.5)
        message=machineendefence(tentative,nombreadeviner)
        print(message+"\n")
        if message=="Trop petit !":
            debutTab=tentative+1
        else:
            finTab=tentative-1
        essai=essai+1 
    #-----------Fin de dichotomie---------------------
    #calcule des scores et enregistrement dans un fichier
    score=Score(essai,joueur1,joueur2)
    print(f"Le joueur {score[1][0]} à gagné {score[1][1]} pts\nLe joueur {score[0][0]} à gagné {score[0][1]} pts")
    return (score)

def machineContreMachineAttaqueAleatoire():
    """
    Fonction qui correspond au programme principale du jeu devinette machine en mode aléotoire contre humain
    Entrée : rien
    Sortie : tableau de tableau de chaine de caractere qui corespond au score finale
    """
    message:str
    essai : int
    tentative : int #nombre entré par le joueur
    score : list[list[str]]
    joueur1 : str
    joueur2 : str
    nombreadeviner:int
    intervmin:int
    intervmax:int
    nombreadeviner=-1#initialisation, cette valeur ne correspond a rien
    message=""
    reglesdevinette()
    print()
    joueur1="Machine message" #défence
    joueur2="Machine chercheur" #attaque
    print()
    print("La limite de l'intervale de nombre est conpris entre 0 et ",Limite)
    print()
    essai=0
    print("La limite de l'intervale de nombre est ",Limite)
    nombreadeviner=machinegenerernombrealeatoire(0,Limite)
    print("Le nombre à deviner est "+str(nombreadeviner))
    print(("\n")*100)#saute des lignes pour cacher le nombre a deviner
    print("La limite de l'intervale de nombre est ",Limite)
    intervmin=1
    intervmax=Limite
    while message!="C'est gagner !":
        sleep(1.5)
        tentative=randint(intervmin,intervmax)
        message=machineendefence(tentative,nombreadeviner)
        print(message+"\n")
        if message=="Trop petit !":
            intervmin=tentative+1
        else:
            intervmax=tentative-1
        
        essai=essai+1 
    #calcule des scores et enregistrement dans un fichier
    score=Score(essai,joueur1,joueur2)
    print(f"Le joueur {score[1][0]} à gagné {score[1][1]} pts\nLe joueur {score[0][0]} à gagné {score[0][1]} pts")
    return (score)

def saisirNom(affichage:str)->str:
    """Fonction qui demande à l'utilisateur d'entres son nom
    
    Args:
        affichage (str): message à afficher à l'écran
        
    Returns:
        str: le nom d'utilisateur
    """
    saisie:str
    print("\n"+affichage)
    saisie=input("Saisie : ")
    return saisie

def test():
    """Precédure qui testes les temps d'execution des fonctions "machineContreMachineAttaqueStrategique" et "machineContreMachineAttaqueAleatoire"
    """
    i:int
    j:int
    tabAlea:list[float]
    tabStrat:list[float]
    temps1:float
    temps2:float
    moyenneAlea:float
    moyenneStrat:float
    tabAlea=[0]*Nbtests
    tabStrat=[0]*Nbtests
    moyenneStrat=0.0
    moyenneAlea=0.0
    for i in range (Nbtests):
        temps1=time()
        print(machineContreMachineAttaqueStrategique())
        temps2=time()
        tabStrat[i]=temps2-temps1
        moyenneStrat=moyenneStrat+tabStrat[i]
    for j in range(Nbtests):
        temps1=time()
        print(machineContreMachineAttaqueAleatoire())
        temps2=time()
        tabAlea[j]=temps2-temps1
        moyenneAlea=moyenneAlea+tabAlea[j]
    moyenneAlea=moyenneAlea/Nbtests
    moyenneStrat=moyenneStrat/Nbtests
    print("Voici les temps d'éxecution du modes aléatoire\n",tabAlea,"\nPour une moyenne de ",moyenneAlea)
    print("Voici les temps d'éxecution du modes Stratégique\n",tabStrat,"\nPour une moyenne de ",moyenneStrat)
    
    
        

if __name__=="__main__":
    print(choixmodejeu())
    #test()
    
    
    







