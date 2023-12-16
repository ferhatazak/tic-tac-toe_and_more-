from morpion import choixdesjeuxmorpion as morpion
from progallumette import principaleallumette as allumettes
from devinette import choixmodejeu as devinette
from puissance4 import principalpuissance4 as puissance4
from BaseDeDonnee_py import Bdd

classbdd:Bdd
classbdd = Bdd("Base/scores.db")

def aff(tab:list[str]):# la syntaxe list[str] et la notation de python pour declarer le type d'un tableau de tuple
    """
    Affiche sous forme d'une chaine de caractere un tableau de tableau5
    ENTREE : Tableau de tuple contenant une chaine et un entier
        contenant le nom du joueur et son score :
        de la forme [ (str,int) , (str,int) , ... ]
    SORTIE : Rien
    """
    i:int
    affichage:str
    affichage="Les scores sont affiche au format\nJoueur, Scores\n\n"
    if tab==[] or tab==[""]:
        print("Il n'y a pas de score enregistré pour ce jeu !\n[]")
    else:
        for i in range (len(tab)):
            affichage=affichage+"--> "+tab[i][0]+", "+str(tab[i][1])+"\n"
        print(affichage)
    print("Les scores sont affichés au dessus !")

def enr_score(score:list[list[str]],nb:int):# la syntaxe list[str] et la notation de python pour declarer le type d'un tableau de tuple
    i:list[str]
    arg1:str
    arg2:int
    for i in score: #i prend succesivement la valeurs de chaque petit tableau [[joueur1,score1],[joueur2,score2]]
        arg1=str(i[0])
        arg2=int(i[1])
        if nb==1:
            classbdd.inserer_score_MORPION(arg1,arg2)
        if nb==2:
            classbdd.inserer_score_ALLUMETTE(arg1,arg2)
        if nb==3:
            classbdd.inserer_score_DEVINETTE(arg1,arg2)
        if nb==4:
            classbdd.inserer_score_PUISSANCE4(arg1,arg2)

def affichemenuscores():
    """
    Procedure qui affiche le menu des scores et appelle le fonction "ChoisirScore"
    qui demande à l'utilisateur d'agir en fonction
    Entree : Rien
    Sortie : Rien
    """
    print("bienvenue dans le menu d'affichage des scores")
    print("1- afficher les scores du morpion")
    print("2- afficher les scores du jeu des allumettes")
    print("3- afficher les scores du jeu des devinettes")
    print("4- afficher les scores du jeu du puissance 4")
    print("5- Quitter\n")

def ChoisirScores()->list[str]:
    """
    Fonction qui demande à l'utilisateur d'entrer un entier qui correspond à l'action qu'il souhaite faire
    Entree : rien
    Sortie : Liste du tuple correspondant aux joueurs et à leurs scores associé

    """
    choix:int
    affichage:list[str]#notation de python pour declarer un tableau de tuple
    affichage=[""]
    choix = 0
    while choix<=0 or choix>5:
        choix = int(input("Saisissez le nombre correspondant : "))
        print()
    if choix == 1 :
        affichage=classbdd.afficher_score_MORPION()
    if choix == 2 :
        affichage=classbdd.afficher_score_ALLUMETTE()
    if choix == 3 :
        affichage=classbdd.afficher_score_DEVINETTE()
    if choix == 4 :
        affichage=classbdd.afficher_score_PUISSANCE4()
    return affichage
#....................................................................................................
#Debut des fonctions pour le trie des scores
#
def ChoisirScoresatrier():
    """
    Procedure qui demande à l'utilisateur d'entrer un entier qui correspond à l'action qu'il souhaite faire
    Entree : rien
    Sortie : rien

    """
    saisie:int
    affichage:list[str]#affichage:list[tuple(str,int)] n'est pas accepté
    affichage=[""]
    saisie = 0
    while saisie<=0 or saisie>5:
        saisie = int(input("Saisissez le nombre correspondant : "))
        print()
    if saisie!=5:
        if saisie == 1 :
            affichage=classbdd.trier_score_MORPION()
        if saisie == 2 :
            affichage=classbdd.trier_score_ALLUMETTE()
        if saisie == 3 :
            affichage=classbdd.trier_score_DEVINETTE()
        if saisie == 4 :
            affichage=classbdd.trier_score_PUISSANCE4()
        aff(affichage)
        print("Et sont triés")

def triagedesscores():
    """
    procedure qui affiche le menu du tri des scores

    Entree :  Rien
    Sortie :  Rien

    """
    print("Bienvenue dans le menu de trie des scores\nIl sera affiché au format \"ligne - nom du joueur, score\"")
    print("1- trier les scores du morpion")
    print("2- trier les scores du jeu des allumettes")
    print("3- trier les scores du jeu des devinettes")
    print("4- trier les scores du jeu du puissance 4")
    print("5- Quitter")
    print()
#
#Fin du trie des scores
#......................................................................................................

def menu():
    """
    Procédure qui affiche le programme principale
    Entrée : Rien
    Sortie : Rien
    """
    print()
    print("Binevenue dans le menu")
    print("1- Jouer au Morpion")
    print("2- Jouer au jeu des allumettes")
    print("3- Jouer au jeu des devinettes")
    print("4- Jouer au jeu de puissance 4")
    print("5- Afficher les scores")
    print("6- trier les scores")
    print("7- Quitter")
    print()


if __name__=="__main__":
    """
    programme qui appelle la procédure qui affiche le menu principale,
    qui appelle la fonction demandé par l'utilisateur et qui affiche a l'ecran le ou les resultats obtenu

    Entrer :  rien
    Sortie :  rien
    """
    saisie:int
    score:list[list[str]]
    affichage:list[str]#notation de python pour declarer un tableau de tuple
    saisie = 0
    while saisie != 7 :
        saisie = 0
        menu()
        while saisie<=0 or saisie>7:
            saisie = int(input("Saisissez le nombre correspondant : "))
            print()
        if saisie == 1 :
            score=morpion()
            enr_score(score,saisie)
        if saisie == 2 :
            score=allumettes()
            enr_score(score,saisie)
        if saisie == 3 :
            score=devinette()
            enr_score(score,saisie)
        if saisie == 4:
            score=puissance4()
            enr_score(score,saisie)

        if saisie == 5 :
            affichemenuscores()#affiche le menu des scores
            affichage=ChoisirScores()#l'utilisateur choisi le jeu dont il souhaite voir le score
            if affichage!=[""]:
                aff(affichage)
        if saisie == 6 :
            triagedesscores()#procedure qui affiche le menu du tri des scores
            ChoisirScoresatrier()#l'utilisateur choisi le jeu dont il souhaite trier le score

    print("Au revoir !")


    #print(type(affichage))
    #print(type(affichage[0]))
    #print(type(affichage[0][0]))
    #print(type(affichage[0][1]))