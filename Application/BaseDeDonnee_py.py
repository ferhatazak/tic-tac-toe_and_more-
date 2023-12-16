import sqlite3

class Bdd:
    def __init__(self, chemin_bdd:str):
        self.chemin_bdd = chemin_bdd

    def afficher_score_MORPION(self)->list[str]:
        """
        Fonction permettant de recuperer les scores de la table MORPION
        ENTREE : Rien
        SORTIE : tableau de tuple de chaine et d'entier
            typé par python au format list[str]
            mais qui se comporte bien comme un tableau de tuple
        """
        connexion:sqlite3.Connection
        curseur:sqlite3.Cursor
        requete_sql:str
        resultat:sqlite3.Cursor
        result:list[str]
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = """SELECT Joueur,Score FROM MORPION;"""
        resultat = curseur.execute(requete_sql)
        result = resultat.fetchall()
        connexion.close()
        return result
    
    def afficher_score_ALLUMETTE(self)->list[str]:
        """
        Fonction permettant de recuperer les scores de la table ALLUMETTE 
        ENTREE : Rien
        SORTIE : tableau de tuple de chaine et d'entier
            typé par python au format list[str]
            mais qui se comporte bien comme un tableau de tuple
        """
        connexion:sqlite3.Connection
        curseur:sqlite3.Cursor
        requete_sql:str
        resultat:sqlite3.Cursor
        result:list[str]
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = """SELECT Joueur,Score FROM ALLUMETTE;"""
        resultat = curseur.execute(requete_sql)
        result = resultat.fetchall()
        connexion.close()
        return result
    
    def afficher_score_DEVINETTE(self)->list[str]:
        """
        Fonction permettant de recuperer les scores de la table DEVINETTE 
        ENTREE : Rien
        SORTIE : tableau de tuple de chaine et d'entier
            typé par python au format list[str]
            mais qui se comporte bien comme un tableau de tuple
        """
        connexion:sqlite3.Connection
        curseur:sqlite3.Cursor
        requete_sql:str
        resultat:sqlite3.Cursor
        result:list[str]
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = """SELECT Joueur,Score FROM DEVINETTE;"""
        resultat = curseur.execute(requete_sql)
        result = resultat.fetchall()
        connexion.close()
        return result
    
    def afficher_score_PUISSANCE4(self)->list[str]:
        """
        Fonction permettant de recuperer les scores de la table MORPION
        ENTREE : Rien
        SORTIE : tableau de tuple de chaine et d'entier
            typé par python au format list[str]
            mais qui se comporte bien comme un tableau de tuple
        """
        connexion:sqlite3.Connection
        curseur:sqlite3.Cursor
        requete_sql:str
        resultat:sqlite3.Cursor
        result:list[str]
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = """SELECT Joueur,Score FROM PUISSANCE4;"""
        resultat = curseur.execute(requete_sql)
        result = resultat.fetchall()
        connexion.close()
        return result
    
    def trier_score_MORPION(self)->list[str]:
        """
        Fonction permettant de recuperer les scores de la table MORPION et de les trier dans l'ordre décroissant 
        ENTREE : Rien
        SORTIE : tableau de tuple de chaine et d'entier
            typé par python au format list[str]
            mais qui se comporte bien comme un tableau de tuple
        """
        connexion:sqlite3.Connection
        curseur:sqlite3.Cursor
        requete_sql:str
        resultat:sqlite3.Cursor
        result:list[str]
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = """SELECT Joueur,Score FROM MORPION ORDER BY Score DESC;"""
        resultat = curseur.execute(requete_sql)
        result = resultat.fetchall()
        connexion.close()
        return result
    
    def trier_score_ALLUMETTE(self)->list[str]:
        """
        Fonction permettant de recuperer les scores de la table ALLUMETTE et de les trier dans l'ordre décroissant 
        ENTREE : Rien
        SORTIE : tableau de tuple de chaine et d'entier
            typé par python au format list[str]
            mais qui se comporte bien comme un tableau de tuple
        """
        connexion:sqlite3.Connection
        curseur:sqlite3.Cursor
        requete_sql:str
        resultat:sqlite3.Cursor
        result:list[str]
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = """SELECT Joueur,Score FROM ALLUMETTE ORDER BY Score DESC;"""
        resultat = curseur.execute(requete_sql)
        result = resultat.fetchall()
        connexion.close()
        return result
    
    def trier_score_DEVINETTE(self)->list[str]:
        """
        Fonction permettant de recuperer les scores de la table DEVINETTE et de les trier dans l'ordre décroissant 
        ENTREE : Rien
        SORTIE : tableau de tuple de chaine et d'entier
            typé par python au format list[str]
            mais qui se comporte bien comme un tableau de tuple
        """
        connexion:sqlite3.Connection
        curseur:sqlite3.Cursor
        requete_sql:str
        resultat:sqlite3.Cursor
        result:list[str]
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = """SELECT Joueur,Score FROM DEVINETTE ORDER BY Score DESC;"""
        resultat = curseur.execute(requete_sql)
        result = resultat.fetchall()
        connexion.close()
        return result

    def trier_score_PUISSANCE4(self)->list[str]:
        """
        Fonction permettant de recuperer les scores de la table PUISSANCE4 et de les trier dans l'ordre décroissant 
        ENTREE : Rien
        SORTIE : tableau de tuple de chaine et d'entier
            typé par python au format list[str]
            mais qui se comporte bien comme un tableau de tuple
        """
        connexion:sqlite3.Connection
        curseur:sqlite3.Cursor
        requete_sql:str
        resultat:sqlite3.Cursor
        result:list[str]
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = """SELECT Joueur,Score FROM PUISSANCE4 ORDER BY Score DESC;"""
        resultat = curseur.execute(requete_sql)
        result = resultat.fetchall()
        connexion.close()
        return result
    
    def inserer_score_MORPION(self,arg1:str,arg2:int)->list[str]:
        """
        Fonction d'ajouter des nouveaux scores dans la table MORPION 
        ENTREE : Chaine de caractere (nom du joueur) et un entier (le score)
        SORTIE : tableau vide typer par python en list[str]
        """
        connexion:sqlite3.Connection
        curseur:sqlite3.Cursor
        requete_sql:str
        resultat:sqlite3.Cursor
        result:list[str]
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""INSERT INTO MORPION (Joueur,Score) VALUES('{arg1}','{arg2}');"""
        resultat = curseur.execute(requete_sql)
        result = resultat.fetchall()
        connexion.commit()
        connexion.close()
        return result
    
    def inserer_score_ALLUMETTE(self,arg1:str,arg2:int)->list[str]:
        """
        Fonction d'ajouter des nouveaux scores dans la table ALLUMETTE  
        ENTREE : Chaine de caractere (nom du joueur) et un entier (le score)
        SORTIE : tableau vide typer par python en list[str]
        """
        connexion:sqlite3.Connection
        curseur:sqlite3.Cursor
        requete_sql:str
        resultat:sqlite3.Cursor
        result:list[str]
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""INSERT INTO ALLUMETTE (Joueur,Score) VALUES('{arg1}','{arg2}');"""
        resultat = curseur.execute(requete_sql)
        result = resultat.fetchall()
        connexion.commit()
        connexion.close()
        return result
    
    def inserer_score_DEVINETTE(self,arg1:str,arg2:int)->list[str]:
        """
        Fonction d'ajouter des nouveaux scores dans la table DEVINETTE
        ENTREE : Chaine de caractere (nom du joueur) et un entier (le score)
        SORTIE : tableau vide typer par python en list[str]
        """
        connexion:sqlite3.Connection
        curseur:sqlite3.Cursor
        requete_sql:str
        resultat:sqlite3.Cursor
        result:list[str]
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""INSERT INTO DEVINETTE (Joueur,Score) VALUES('{arg1}','{arg2}');"""
        resultat = curseur.execute(requete_sql)
        result = resultat.fetchall()
        connexion.commit()
        connexion.close()
        return result

    def inserer_score_PUISSANCE4(self,arg1:str,arg2:int)->list[str]:
        """
        Fonction d'ajouter des nouveaux scores dans la table PUISSANCE4 
        ENTREE : Chaine de caractere (nom du joueur) et un entier (le score)
        SORTIE : tableau vide typer par python en list[str]
        """
        connexion:sqlite3.Connection
        curseur:sqlite3.Cursor
        requete_sql:str
        resultat:sqlite3.Cursor
        result:list[str]
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""INSERT INTO PUISSANCE4 (Joueur,Score) VALUES('{arg1}','{arg2}');"""
        resultat = curseur.execute(requete_sql)
        result = resultat.fetchall()
        connexion.commit()
        connexion.close()
        return result