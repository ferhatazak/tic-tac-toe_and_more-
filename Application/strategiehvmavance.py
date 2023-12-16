
from math import inf as infinity
from random import choice
import platform
import time
from os import system


HUMAN = -1
COMP = +1
tableau = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def evaluation(state : list[str]) -> int:
    """
    Fonction qui attribut le score

    """
    if victoire(state, COMP):
        score = +1
    elif victoire(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def victoire(state : list[str], joueur : int ) -> bool:
    """
    fonction qui teste si un joueur spécifique remporte la victoire.
    elle retourne un booleen 
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [joueur, joueur, joueur] in win_state:
        return True
    else:
        return False


def defaite(state : list[str]) -> bool:
    """
    fonction permettant de savoir qui gagne entre l'HOMME ou la MACHINE. Elle retourne 
    un booleen.
    Entree : tableau de chaine de caractere 
    Sortie : booleen
    """
    return victoire(state, HUMAN) or victoire(state, COMP)


def case_vide(state : list[str]) -> list[list[int]]:
    """
    Fonction permettant de remplir une case vide, elle retourne un tabelau de chaine de caractere.
    Entree : tableau de chaine de caractere
    Sortie : tableau de tableau d'entier


    """
    cells : list[list[int]]
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def mouvement_ok(x : int, y : int ) -> bool:
    """
    Fonction qui verifie si le mouvement est possible.
    Elle retourne un booleen 
    Entree : entier
    Sortie : booleen
    """
    if [x, y] in case_vide(tableau):
        return True
    else:
        return False


def positionner_movement(x : int , y : int , joueur : int) -> bool:
    """
   fonction qui définie le mouvement sur le tableau, si les coordonnées sont valides
   Entree : entier
   Sortie : booleen
    """
    if mouvement_ok(x, y):
        tableau[x][y] = joueur
        return True
    else:
        return False


def strategie(state : list[str], n : int, joueur : int) -> list[int]:
    """
    Fonction qui correspond à la strategie de l'IA. 
    Entrée : tableau de chaine de caracteres, entier
    Sortie : tableau de chiane de caracteres
    """
    best : list[int]
    if joueur == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if n == 0 or defaite(state):
        score = evaluation(state)
        return [-1, -1, score]

    for cell in case_vide(state):
        x, y = cell[0], cell[1]
        state[x][y] = joueur
        score = strategie(state, n - 1, -joueur)
        state[x][y] = 0
        score[0], score[1] = x, y

        if joueur == COMP:
            if score[2] > best[2]:
                best = score  # valeur max
        else:
            if score[2] < best[2]:
                best = score  # valeur minimum

    return best


def clean():
    """
    Procédure permettant de nettoyer le terminal 
    Entree : rien 
    Sortie : rien 
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def rendu(state : list[str], c_choice : str, h_choice : str):
    """
    Procedure permettant d'afficher un tableau qui correspond au tableau du jeu du morpion.
    Entree : tableau de chaine de caractere, caractere
    Sortie : rien 
    """

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def choix_ia(c_choice : str, h_choice : str) -> None:
    """
    procedure qui permet a l'ia de choisir une case.
    Entrée : chaine de caractere 
    Sortie : null
    """
    move : list[str]
    n = len(case_vide(tableau))
    if n == 0 or defaite(tableau):
        return

    clean()
    print(f'Marque machine [{c_choice}]')
    rendu(tableau, c_choice, h_choice)

    if n == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = strategie(tableau, n, COMP)
        x, y = move[0], move[1]

    positionner_movement(x, y, COMP)
    time.sleep(1)


def mouvhomme(c_choice : str, h_choice : str) -> None:
    """
    Fonction permettant à l'HOMME de choisir une case
    Entree : chaine de caractere 
    Sortie : null
    """
    n = len(case_vide(tableau))
    if n == 0 or defaite(tableau):
        return

    # tout les mouvements valides
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'marque Homme [{h_choice}]')
    rendu(tableau, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Entrez le numero de la case (1..9): '))
            coord = moves[move]
            can_move = positionner_movement(coord[0], coord[1], HUMAN)

            if not can_move:
                print('mouvement impossible')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('au revoir')
            exit()
        except (KeyError, ValueError):
            print('Mauvais choix')


def principalehvmstrat():
    """
    Procedure qui correspond au programme principale du jeux morpion homme contre machine 
    avec difficulté avancé.
    Entree : rien 
    Sortie : rien 
    """
    clean()
    h_choice = ''  # X ou O
    c_choice = ''  # X ou O
    first = ''  # si l'homme commence 

    # l'homme choisi X ou O pour jouer 
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choisissez votre marque: X ou O\n----> ').upper()
        except (EOFError, KeyboardInterrupt):
            print('au revoir')
            exit()
        except (KeyError, ValueError):
            print('Mauvais choix')

    # Réglage du choix de l'ordinateur
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # l'Homme choisi de commencer 
    clean()
    while first != 'HOMME' and first != 'MACHINE':
        try:
            first = input('Saisissez qui commence en majuscule[HOMME/MACHINE]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('au revoir')
            exit()
        except (KeyError, ValueError):
            print('Mauvais choix')

    # Boucle principale de ce jeu
    while len(case_vide(tableau)) > 0 and not defaite(tableau):
        if first == 'MACHINE':
            choix_ia(c_choice, h_choice)
            first = ''

        mouvhomme(c_choice, h_choice)
        choix_ia(c_choice, h_choice)

    # fin partie message 
    if victoire(tableau, HUMAN):
        clean()
        print(f'marque HOMME [{h_choice}]')
        rendu(tableau, c_choice, h_choice)
        print('vous avez gagne!')
    elif victoire(tableau, COMP):
        clean()
        print(f'marque ia [{c_choice}]')
        rendu(tableau, c_choice, h_choice)
        print('vous avez perdu!')
    else:
        clean()
        rendu(tableau, c_choice, h_choice)
        print('egalité!')

    exit()


if __name__ == '__main__':
    principalehvmstrat()
