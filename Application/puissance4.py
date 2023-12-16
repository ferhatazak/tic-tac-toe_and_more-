
def reglepuissance():
    print("Le but du jeu est d'aligner une suite de 4 pions de même couleur sur une grille comptant 6 rangées et 7 colonnes.")
    print("Chaque joueur dispose de 21 pions d'une couleur.")
    print("Tour à tour; les deux joueurs placent un pion dans la colone de leur choix,")
    print("le pion coulisse alors jusqu'à la position la plus basse possible")
    print("dans ladite colonne à la suite de quoi c'est à l'adversaire de jouer.")
    print("Le vainqueur est le joueur qui réalise le premier un alignement (horizontal, vertical ou diagonal) consécutif d'au moins quatre pions de sa couleur.")
    print("Si, alors que toutes les cases de la grille de jeu sont remplies, aucun des deux joueurs n'a réalisé un tel alignement,")
    print("la partie est déclarée nulle.")

def creematrice(cases:list[int])->list[list[str]]:
    """
    Fonction qui creer une matrice
    ENTREE : entier
    SORTIE : La matrice = tableau contenant des tableau de chaine de caractere(tableau de 6 lignes contenant 7 espaces)
    """
    i:int
    tabmatrice:list[list[str]]
    tabmatrice=[[""]]*cases[0] #tableau de 6 lignes
    for i in range(cases[0]):#7 colonnes par lignes
       tabmatrice[i]=[" "]*cases[1]
    return(tabmatrice)

def affichermatrice(matrice:list[list[str]]):
    """
    Procédure qui affiche un tableau matriciel sous la forme d'une grille de puissance 4 au format d'une chaine de caractere
    ENTREE : tableau de tableau contenant une chaine de caracteres
    SORTIE : Rien

    """
    affichage:str
    i:int
    indice:int
    barre=" | "
    affichage="   "
    for nombre in range(1,len(matrice[0])+1): #on prend 0 par exemple comme tous les tableau a l'interieure du tableau matriciel sont de meme taille
        affichage=affichage+str(nombre)+"   "
    affichage=affichage+"\n\n"
    for i in range(len(matrice)): #colonnes
        for indice in range(len(matrice[i])):#lignes
            affichage=affichage+barre+str(matrice[i][indice])
        affichage=affichage+barre+"\n -----------------------------\n"
    print("\n"+affichage)

def ajoutermarque(matrice:list[list[str]],tour:int,nom_nbr_de_case:list[int],lejoueur:list[str])->list[list[str]]:
    """
    Fonction qui permet d'ajouter une marque
    ENTREE : la matrice = tableau de tableau de caracteres , le tour qui correspond au joueur qui doit jouer
    SORTIE : la matrice + la marque ajoute
    """
    marque:str
    saisie:int
    indice:int
    marqueOK:bool
    affichage:str
    marqueOK=False
    affichage=""
    if tour==1:
        marque="J" #pour jaune
    else:
        marque="R"#pour rouge

    while marqueOK==False:
        indice=nom_nbr_de_case[0]-1
        saisie=0
        while saisie>7 or saisie<1 :
            affichage="Entrez le numero de colonne, joueur "+str(lejoueur[tour])+" (qui a le couleur \""+str(marque)+"\") : "

            saisie=int(input(affichage))
            if saisie>7 or saisie<1:
                print("erreur, entrez un numero de colonne valide")
        while matrice[indice][saisie-1]!=" " and indice>0: #indice = numéro de ligne
            indice=indice-1
        if indice>=0 and (matrice[indice][saisie-1]!="J" and matrice[indice][saisie-1]!="R"):
            matrice[indice][saisie-1]=marque
            marqueOK=True

        elif indice==0 and marqueOK==False:
            print("erreur la colone est pleine")
    return matrice

def config_du_fin_de_jeu(tabmatrice:list[list[str]],tour:int,dimension:list[int])->bool:
    """
    Fonction qui verifie la configuration des marques du tableau matriciel et indique si la partie est ou non finie
    Entrée : tableau de tableau de chaine de caractere, le tour qui correspond au joueur qui doit jouer et les dimentions du plateau de jeu
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
    j=0
    ligne=dimension[0]
    i=0
    colonne=dimension[1]
    gagnecolonne=False
    gagnediagonale=False
    finjeu=False
    if tour==1:
        marque="J" #pour jaune
    else:
        marque="R"#pour rouge

    #Gagner horizontalement
    for i in range(colonne-3):
        for j in range(ligne):
            if tabmatrice[j][i] == marque and tabmatrice[j][i+1] == marque and tabmatrice[j][i+2] == marque and tabmatrice[j][i+3] == marque:
                gagneligne=True

    # Gagner verticalement
    if gagneligne!=True:
        for i in range(colonne):
            for j in range(ligne-3):
                if tabmatrice[j][i] == marque and tabmatrice[j+1][i] == marque and tabmatrice[j+2][i] == marque and tabmatrice[j+3][i] == marque:
                    gagnecolonne=True

        #Gagner en diagonale montante depuis en bas a gauche jusqu'à en haut a droite)
        if gagnecolonne!=True:
            for i in range(colonne-3):
                for j in range(3, ligne):
                    if tabmatrice[j][i] == marque and tabmatrice[j-1][i+1] == marque and tabmatrice[j-2][i+2] == marque and tabmatrice[j-3][i+3] == marque:
                        gagnediagonale=True

            #Gagner en diagonale descendante (depuis en haut a gauche jusqu'à en bas a droite)
            if gagnediagonale!=True:
                for i in range(colonne-3):
                    for j in range(ligne-3):
                        if tabmatrice[j][i] == marque and tabmatrice[j+1][i+1] == marque and tabmatrice[j+2][i+2] == marque and tabmatrice[j+3][i+3] == marque:
                            gagnediagonale=True
    if  gagneligne==True or gagnecolonne==True or gagnediagonale==True:
        finjeu=True
    return finjeu

def defscore(nbcoup:int,joueur:list[str],tour:int,partiegagne:bool)->list[list[str]]:
    """
    Fonction qui attibue les scores a chaques joueurs en fonction de leur nombre de coup\n
    ENTREE : entier qui corespond au nombre de coup,
    \n         la liste des joueurs sous forme de liste de chaine de caractere
    \n         et le booleen qui undique vrai si la partie est fini

    SORTIE : tableau de tableau de chaine de caractere
    """
    i:int
    tabscore:list[list[str]]
    gagnant:int
    if tour==1:#tour designe le perdant
        gagnant=0
    else:
        gagnant=1
    tabscore=[["",""],["",""]]
    i=0
    if partiegagne==True:
        tabscore[0][0]=joueur[gagnant]
        while i!=nbcoup and i!=nbcoup-1:
            i=i+2#le premier joueur aura toujours un coup d'avance sur le deuxieme. Pour au 2 joueur d'avoir le meme score s'il cagne, on utilise i
        tabscore[0][1]=str(int(4200/i))
        tabscore[1][0]=joueur[tour]
        tabscore[1][1]="10"
    else:
        tabscore[0][0]=joueur[gagnant]
        tabscore[0][1]="80"
        tabscore[1][0]=joueur[tour]
        tabscore[1][1]="80"
    print(f"Le joueur {tabscore[0][0]} à gagné {tabscore[0][1]} pts\nLe joueur {tabscore[1][0]} à gagné {tabscore[1][1]} pts")
    return tabscore





def principalpuissance4():
    """
    fonction qui fait office de programme principale pour le puissance 4
    ENTREE : Rien
    SORTIE : tableau de tableau de chaine de caractere, qui correspond au score.
    """

    reglepuissance()
    print()
    Nbcase=[6,7] #constante qui represente 6 lignes, 7 colonnes
    tableau:list[list[str]]
    score:list[list[str]]
    tour:int
    finjeu:bool
    joueur1:str
    joueur2:str
    joueur:list[str]
    cpt:int
    cpt=0
    tour=0
    finjeu=False
    joueur1=input("Entrez votre nom joueur 1 : ")
    joueur2=input("Entrez votre nom joueur 2 : ")
    joueur=[joueur1,joueur2]
    tableau=creematrice(Nbcase)
    affichermatrice(tableau)

    while cpt!=42 and finjeu!=True:
        tableau=ajoutermarque(tableau,tour,Nbcase,joueur)
        affichermatrice(tableau)
        if cpt>=6:
            finjeu=config_du_fin_de_jeu(tableau,tour,Nbcase)

            if tour==1:
                tour=0
            else:
                tour=1
                cpt=cpt+1
    score=defscore(cpt,joueur,tour,finjeu)#le nombre tour designe maintenant le perdant
    print("Fin de partie")
    return score

        
        




if __name__ == "__main__":
    print(principalpuissance4())



