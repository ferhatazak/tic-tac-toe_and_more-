import copy

## Permet d'afficher la grille
def Affiche(liste : list[str]):
    """
    procedure permettant d'afficher une grille du jeu puissance 4
    Entree : tableau de chaine de caractere
    Sortie : rien 
    """
    resultat=""
    #grille de 6 lignes
    for i in range(6):
        resultat+="| "
        #et de 12 colonnes
        for j in range(12):
            resultat=resultat+str(liste[i][j])+" | "
        resultat+="\n"
    resultat+=" --- --- --- --- --- --- --- --- --- --- --- --- "
    resultat+="\n  1   2   3   4   5   6   7   8   9   10  11  12  "
    print(resultat)


def Action(s : list[str]) -> list[str] :
    """
    fonction qui Permet de faire la liste de tous les coups possibles selon la grille de jeu passée en parametre
    entree :  s est la grille de jeu
    sortie : Retourne une liste de liste des actions possibles, où chaque liste de liste est une liste de 2 cases qui stock [abscisse, ordonnée] de chaque coup possible
    """
    actions=[]
    #On va parcourir la grille en allant de colonne en colonne
    for j in range(12):
        # On parcour ensuite les lignes de bas en haut
        for i in range(5, -1, -1):
            if (s[i][j]==' '):
                # Si la case est vide on stock ses coordonées
                actions.append([i,j])
                # Et on passe a la colonne suivante
                break
    return actions
 

def Result(s,a,player : str):
    """
    fonction permettant d'appliquer l'action (entree :)  a, au joueur player, sur la grille s
    sortie  : retourne la grille nextState où l'action a, a été appliqué sur la grille s par le joueur player
    """
    # On créer une  copy de la grille
    nextState=copy.deepcopy(s)
    # On modifie la case en question
    nextState[a[0]][a[1]]=player
    return nextState
 
    

def TerminalTest(s):
    """
    fonction qui permet de savoir quand le jeu est fini soit il y a un gagant, soit les 42 pions sont posés
    entree : la grille de jeu à évaluer
    sortie  : Returne True si le jeu est finis, false sinon
    """
    compteur = 0
    char = 'X'
    charoppose = 'O'
    chartemp = ''
    ##Row
    ## On verifie si l'un des joueurs fait un alignement
    ## On vérifie les alignement des lignes
    for i in s:
        compteur = 0
        ## On parcours de colonne en colonne
        for j in i:
            ## Si on tombe sur un char on rajoute 1 au compteur
            if(j == char):
                compteur += 1
            ## Si on tombe sur le char adverse, on intervertit char et 
            ## charoppose et on met le compteur a 1
            elif (j == charoppose):
                compteur = 1
                chartemp = copy.deepcopy(char)
                char = copy.deepcopy(charoppose)
                charoppose = copy.deepcopy(chartemp)
            ## Si on tombe sur une case vide on met le compteur a zero
            elif (j == ' '):
                compteur = 0
            ## Si le compteur vaut 4, le jeu est finis on return True
            if (compteur == 4):
                return True
            
    ##Column
    ## Pareil que pour les lignes mais en colonnes
    ## On parcours les colonnes
    for j in range(12):
        compteur = 0
        # Puis les lignes
        for i in range(6):
            if(s[i][j] == char):
                compteur += 1
            elif (s[i][j] == charoppose):
                compteur = 1
                chartemp = copy.deepcopy(char)
                char = copy.deepcopy(charoppose)
                charoppose = copy.deepcopy(chartemp)
            elif (s[i][j] == ' '):
                compteur = 0
            if (compteur == 4):
                return True
    
    ##Diagonal croissante
    ## Permet de vérifier les 2 premières diagonales croissantes du jeu
    ##(a gauche de la grille)
    for i in range(3,5):
        compteur = 0
        j = 0
        while(i >= 0):
            if(s[i][j] == char):
                compteur += 1
            elif(s[i][j] == charoppose):
                chartemp = copy.deepcopy(char)
                char = copy.deepcopy(charoppose)
                charoppose = copy.deepcopy(chartemp)
                compteur = 1
            elif (s[i][j] == ' '):
                compteur = 0
            if (compteur == 4):
                return True
            i -= 1
            j += 1
    ## Permet de verifier tous le restes des diagonales croissantes  
    for j in range(10):
        compteur = 0
        i = 5
        while((i >= 0) & (j < 12)):
            if(s[i][j] == char):
                compteur += 1
            elif(s[i][j] == charoppose):
                chartemp = copy.deepcopy(char)
                char = copy.deepcopy(charoppose)
                charoppose = copy.deepcopy(chartemp)
                compteur = 1
            elif (s[i][j] == ' '):
                compteur = 0
            if (compteur == 4):
                return True
            i -= 1
            j += 1
            
    ##Diagonal decroissante
    ## Permet de vérifier les 2 premieres diagonales décroissantes 
    ## (a droite de la grille)
    for i in range(3,5):
        compteur = 0
        j = 11
        while(i >= 0):
            if(s[i][j] == char):
                compteur += 1
            elif(s[i][j] == charoppose):
                chartemp = copy.deepcopy(char)
                char = copy.deepcopy(charoppose)
                charoppose = copy.deepcopy(chartemp)
                compteur = 1
            elif (s[i][j] == ' '):
                compteur = 0
            if (compteur == 4):
                return True
            i -= 1
            j -= 1
    ## Permet de vérifier le reste des diagonales decroissantes        
    for j in range(11, -1, -1):
        compteur = 0
        i = 5
        while((i >= 0) & (j >= 0)):
            if(s[i][j] == char):
                compteur += 1
            elif(s[i][j] == charoppose):
                chartemp = copy.deepcopy(char)
                char = copy.deepcopy(charoppose)
                charoppose = copy.deepcopy(chartemp)
                compteur = 1
            elif (s[i][j] == ' '):
                compteur = 0
            if (compteur == 4):
                return True
            i -= 1
            j -= 1
    
    ## Si tous les pions sont posés
    compteur3 = 0
    ## On parcours la grille
    for i in s:
        for j in i:
            ## Si il y a un pion on rajoute 1 au compteur
            if((j == char) | (j == charoppose)):
                compteur3 += 1
            if (compteur3 == 42):
                return True
    
    return False


def Utility(state : list[str], player : str,p3 : int,p32 : int,p4 : int,p3A : int,p4A : int ) -> int:
    """
    fonction qui permet de donner une valeur a la grille state pour le joueur player

    entree : state : qui est la grille de jeu a évaluer, player : qui est le joueur a qui on va évaluer la utility , p3,p32,p4,p3A,p4A sont des parametres de notre utility qui permette 
    d'apporter plus ou moins d'importance aux alignements de 3 et 4 pions par l'adversaire et le player
    sortie  : Returne result qui est la valeur de la utility

    """
    char : str
    result=0 
    compteur = 0 
    char = player 
    ## On initialise les joueurs
    if (char == 'X') : 
        charoppose = 'O'
    if (char == 'O') : 
        charoppose = 'X'
    ##On affecte un nombre de point a chaque cases en fonction du nombre de 
    ## combinaison de 4 qu'elles peuvent faire, permet d'apporter un poid a 
    ## chaque case
    gridPoint=[[3,4,5,7,7,7,7,7,7,5,4,3],
               [4,6,8,10,12,14,14,12,10,8,6,4],
               [5,8,11,13,15,17,17,15,13,11,8,5],
               [5,8,11,13,15,17,17,15,13,11,8,5],
               [4,6,8,10,12,14,14,12,10,8,6,4],
               [3,4,5,7,12,14,14,12,7,5,4,3]]
    ## On effectue la somme des poids de chaque case remplie par le player
    for i in range(6):
        for j in range(12):
            if(state[i][j] == player):
                result += gridPoint[i][j]
    ##Row
    ## On donne des points pour des alignements de 4 et de 3
    ## On verifie d'abord les alignment du player
    for i in range(6):
        # Permet de stocker la case avant un alignement pour savoir si la case
        # est jouable ou non
        previous = ' '
        compteur = 0
        for j in range(11):
            if(state[i][j] == char):
                compteur += 1
            else:
                compteur = 0
                previous = state[i][j]
            # Si il y a un alignement de 3 et si l'une des cases aux extrémités
            # est vide
            if ((compteur == 3) & ((state[i][j+1] == ' ') | (previous == ' '))):
                result += p3
            # Si il y a un alignement de 3 et si les deux cases aux extrémités
            # sont vides
            if ((compteur == 3) & (state[i][j+1] == ' ') & (previous == ' ')):
                result += p32
            ## Si il y a un alignment de 4, c'est une victoire
            if (compteur == 4):
                result = p4
                
    ## On fait les memes tests mais pour voir les alignements de l'adversaire
    for i in state:
        compteur = 0
        for j in i:
            if(j == charoppose):
                compteur += 1
            else:
                compteur = 0
            ## Si il fait un alignement de 3
            if (compteur == 3):
                result -= p3A
            ## Si il fait un alignement de 4
            if (compteur == 4):
                result = -p4A
                return result
            
    ##Column
    ## On fait les memes testes pour les colonnes
    ## Ici pour le player
    for i in range(12):
        compteur = 0
        for j in range(5,-1,-1):
            if(state[j][i] == char):
                compteur += 1
            else:
                compteur = 0
            # On verifie si le compteur vaut 3 et si la case suivante est vide
            if ((compteur == 3) & (state[j][i-1] == ' ')):
                result += p3
            if (compteur == 4):
                result = p4
    
    ## Ici de meme, mais pour l'adversaire
    for i in range(12):
        compteur = 0
        for j in range(5,-1,-1):
            if(state[j][i] == charoppose):
                compteur += 1
            else:
                compteur = 0
            if (compteur == 3 & j != 0):
                result -= p3A
            if (compteur == 4):
                result = -p4A
                return result
    
    ##Diagonal croissante
    ## On parcour la grille, mais pas en entière, car on va la parcourir dans 
    ## les boucles if
    for i in range(5,2,-1):
        for j in range(0,8):
            ## Pour vérifier les alignement du player
            if (state[i][j]==player):
                ## Alignement de 3
                if((state[i-1][j+1]==player) & (state[i-2][j+2]==player) & (state[i-3][j+3]==' ')):
                    result += p3
                ## Alignement de 4
                if((state[i-1][j+1]==player) & (state[i-2][j+2]==player) & (state[i-3][j+3]==player)):
                    result = p4
            ## Pour vérifier les alignement de l'adversaire
            elif (state[i][j]==charoppose):
                if((state[i-1][j+1]==charoppose) & (state[i-2][j+2]==charoppose)):
                    result -= p3A
                if((state[i-1][j+1]==charoppose) & (state[i-2][j+2]==charoppose) & (state[i-3][j+3]==charoppose)):
                    result = -p4A
                    return result
    
    ##Diagonal decroissante
    ## On parcour la grille, mais pas en entière, car on va la parcourir dans 
    ## les boucles if
    for i in range(5,2,-1):
        for j in range(11,3,-1):
            ## Pour vérifier les alignement du player
            if (state[i][j]==player):
                ## Alignement de 3
                if((state[i-1][j-1]==player) & (state[i-2][j-2]==player) & (state[i-3][j-3]==' ')):
                    result += p3
                    ## Alignement de 4
                if((state[i-1][j-1]==player) & (state[i-2][j-2]==player) & (state[i-3][j-3]==player)):
                    result = p4
            ## Pour vérifier les alignement de l'adversaire
            elif (state[i][j]==charoppose):
                if((state[i-1][j-1]==charoppose) & (state[i-2][j-2]==charoppose)):
                    result -= p3A
                if((state[i-1][j-1]==charoppose) & (state[i-2][j-2]==charoppose) & (state[i-3][j-3]==charoppose)):
                    result = -p4A
                    return result
    
    return result


import time 
##Permet de jouer contre notre IA en jouant en premier
def Jouer(grid):
    joueur = 0
    char = 'X'
    charoppose = 'O'
    ## Temps que le jeu n'est pas finis on continue de jouer
    while(TerminalTest(grid) == False):
        ## Tour du joueur
        if (joueur%2 == 0):
            Affiche(grid)
            print("Tu veux jouer dans quelle colonne?")
            colonne = int(input())-1
            ligne = 0
            ## On cherche dans quelle ligne placer le pion, on parcour les
            ## lignes de haut en bas, si une case est vide on la stock (donc 
            ## quand les cases seront remplie on aura en stock la derniere case
            ## vide)
            for i in range(6):
                if (grid[i][colonne] == ' '):
                    ligne = i
            ## On remplit la grille du coup donné par le joueur
            grid = Result(grid,[ligne, colonne], char)
            joueur += 1
        ## Tour de l'IA
        else:
            ## Permet de stocker le temps
            t0=time.time()
            ##On joue le coup de l'IA           ,p3,p32,p4,p3A,p4A
            action = Alpha_Beta(grid,charoppose,30,60,15000,30,10000)
            ## On affiche la colonne jouée
            print("L'IA a joué en ", (action[1][1] + 1), "ème colonne")
            grid = Result(grid, [action[1][0], action[1][1]], charoppose)
            ## On récupère le temps écoulé pour jouer le coup
            t1=time.time()
            duree = t1-t0
            secondes = round(duree%60)
            ## On affiche la durée du coup
            print("Coup joué en : ", secondes, " secondes")
            joueur += 1
    Affiche(grid)


def Jouer2(grid):
    """
    fonction qui permet de jouer contre l'IA en jouant en deuxieme
    On refait comme ci dessus mais en jouant en deuxieme
    """
    joueur = 0
    char = 'X'
    charoppose = 'O'
    while(TerminalTest(grid) == False):
        if (joueur%2 == 0):
            t0=time.time()
            ##                                  ,p3,p32,p4,p3A,p4A
            action = Alpha_Beta(grid,charoppose,30,60,10000,30,10000)
            print("L'IA a joué en ", (action[1][1] + 1), "ème colonne")
            grid = Result(grid, [action[1][0], action[1][1]], charoppose)
            t1=time.time()
            duree = t1-t0
            secondes = round(duree%60)
            print("Coup joué en : ", secondes, " secondes")
            joueur += 1
        else:
            Affiche(grid)
            print("Tu veux jouer dans quelle colonne?")
            colonne = int(input())-1
            ligne = 0
            for i in range(6):
                if (grid[i][colonne] == ' '):
                    ligne = i
            grid = Result(grid,[ligne, colonne], char)
            joueur += 1
    Affiche(grid)


def Jouer3(grid):
    """
    fonction qui permet de faire jouer l'IA contre lui meme
    On refait comme les deux fonctions précédente mais en jouant ne faisant jouer
    que l'IA
    """
    joueur = 0
    char = 'X'
    charoppose = 'O'
    while(TerminalTest(grid) == False):
        if (joueur%2 == 0):
            t0=time.time()
            ##                                  ,p3,p32,p4,p3A,p4A
            action = Alpha_Beta(grid,charoppose,30,60,10000,30,10000)
            grid = Result(grid, [action[1][0], action[1][1]], charoppose)
            t1=time.time()
            duree = t1-t0
            secondes = round(duree%60)
            print("Coup joué en : ", secondes, " secondes")
            joueur += 1
            Affiche(grid)
        else:
            t0=time.time()
            ##                            ,p3,p32,p4,p3A,p4A
            action = Alpha_Beta(grid,char,20,50,10000,60,200)
            grid = Result(grid,[action[1][0], action[1][1]], char)
            t1=time.time()
            duree = t1-t0
            secondes = round(duree%60)
            print("Coup joué en : ", secondes, " secondes")
            joueur += 1
            Affiche(grid)
    Affiche(grid)



def Alpha_Beta(state,joueur : str ,p3 : int ,p32 : int ,p4 : int ,p3A : int ,p4A : int ):
    """
    Fonction alpha beta qui va renvoyer la valeur V et la coordonnées du pions a placer
    entree : State est la grille vide de depart passée en parametre, Joueur est X ou O
    sortie : Return l'action a jouer et le V
    """
    if(joueur == 'X') : 
        opposant = 'O'
    if(joueur == 'O') : 
        opposant = 'X'
    ## On met renvoyer action a True afin de savoir qu'elle est la meilleurs action
    resultat = Max_Value_Alpha_Beta(state,joueur,opposant,-10000,10000,0,3,p3,p32,p4,p3A,p4A,True)
    return resultat

## Fonction Min-Value (reflexion du tour de l'opposant, veut minimiser utily de joueur)
## State est la grille de jeu passée en parametre
## Joueur est X ou O
## Opposant est l'inverse de joueur
## Alpha et beta sont les bornes de l'elagage alpha beta
## Compteur qui permet de controler la profondeur
## Profondeur permet de savoir quelle va etre la profondeur de notre fonction
def Min_Value_Alpha_Beta(state,joueur,opposant,alpha,beta,compteur,profondeur,p3,p32,p4,p3A,p4A):
    ## Si la grille est dans un état final ou si on a atteint la limite de profondeur
    ## On retourne Utility
    if(TerminalTest(state) | compteur == profondeur) : 
        return Utility(state,joueur,p3,p32,p4,p3A,p4A)
    #valeur infiniment haute
    v = 10000000
    #Ici ce sont les actions de l'opposant qu'on prend car c'est son tour
    for a in Action(state):
        v = min(v,Max_Value_Alpha_Beta(Result(state,a,opposant),joueur,opposant,alpha,beta,compteur+1,profondeur,p3,p32,p4,p3A,p4A))
        if (v <= alpha) : 
            return v
        beta = min(beta,v)
    return v

## Fonction Max-Value (reflexion du tour de joueur, veut maximiser utility de joueur)
## State est la grille de jeu passée en parametre
## Joueur est X ou O
## Opposant est l'inverse de joueur
## Alpha et beta sont les bornes de l'elagage alpha beta
## Compteur qui permet de controler la profondeur
## Profondeur permet de savoir quelle va etre la profondeur de notre fonction
## Renvoyer l'action permet de savoir si il faut retourner V ou V et l'action qui lui est associée
def Max_Value_Alpha_Beta(state,joueur,opposant,alpha,beta,compteur,profondeur,p3,p32,p4,p3A,p4A,renvoyer_action = False):
    if(TerminalTest(state) | compteur == profondeur) : 
        return Utility(state,joueur,p3,p32,p4,p3A,p4A)
    #valeur infiniment basse
    v = -10000000
    ## Permet de renvoyer l'action a la fonction Alpha Beta
    ## c'est le seul moment ou le booléen est True
    ## Permet de stocker l'action afin de la renvoyer
    if(renvoyer_action):
        sauvegarde_action = []
        #Ici ce sont les actions du joueur qu'on prend car c'est son tour
        for a in Action(state):
            ancien_v = v
            v = max(v,Min_Value_Alpha_Beta(Result(state,a,joueur),joueur,opposant,alpha,beta,compteur,profondeur,p3,p32,p4,p3A,p4A))
            if(ancien_v != v): 
                sauvegarde_action=a
            if (v >= beta) : 
                return [v,sauvegarde_action]
            alpha = max(alpha,v)
        return [v,sauvegarde_action]
    #Ici ce sont les actions du joueur qu'on prend car c'est son tour
    for a in Action(state):
        v = max(v,Min_Value_Alpha_Beta(Result(state,a,joueur),joueur,opposant,alpha,beta,compteur+1,profondeur,p3,p32,p4,p3A,p4A))
        if (v >= beta) : 
            return v
        alpha = max(alpha,v)
    return v


#fonction qui stocke dans une variable les meilleurs paramètres de jeu 
#prend en paramètre la grille de jeu à un stade n
#affiche sur la console ces paramètres là après 100 itérations
#repose sur l'utilisation de l'aléatoire pour essayer un maximum de jeu de paramètres différents
import random
def BestParam(grid):
    bestparam=[300,1000,700,2200,3]
    besttemp=0
    for i in range(100):
        p4=random.randrange(100,1000,100)
        p3=random.randrange(0,p4,100)
        p6=random.randrange(10*round((p4-(p4/2))/10), 10*round((p4+(p4/2))/10),100)
        p5 = 0
        while(p5): 
            p5=random.randrange(p3-round(p3/2),p3+round(p3/2),100)
        depth=3
        resultat=Jouer3(grid2,[p3,p4,p5,p6,depth],bestparam)
        print("check")
        if (resultat[0]!=[-1,-1,-1,-1,-1]):
            bestparam=resultat[0]
            besttemp=resultat[1]
            print("victoire")
            print(bestparam)
            print(besttemp)
            print('')
        else:
            print("égalité")
            print(bestparam)
            print(besttemp)
            print('')
        


grid=[[' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ','O','X',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ','O','X','X','X',' ',' ',' ',' '],
      [' ',' ',' ',' ','X','O','O','O',' ',' ',' ',' '],
      [' ',' ',' ',' ','O','X','X','O',' ',' ',' ',' '],
      [' ',' ',' ',' ','O','X','X','O',' ',' ',' ',' ']]
grid2=[[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
def menu():
    print("bienvenu dans le menu des bot")
    print("1 - jouer contre l'ia, vous jouer en premier ")
    print("2 - jouer contre l'ia vous jouer en deuxieme  ")
    print("3 - les deux machine s'affronte  ")
    


if __name__=='__main__' :
    

    menu()
    ##Permet de jouer contre notre IA en jouant en premier
    saisie = int(input("que voulez vous faire :   "))
    if saisie == 1 : 
        Jouer(grid2)
    if saisie == 2 :
    ##Permet de jouer contre l'IA en jouant en deuxieme
        Jouer2(grid2)
    if saisie == 3 :
    ##Permet de faire jouer l'IA contre lui meme
        Jouer3(grid2)
    
