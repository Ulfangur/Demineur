from random import randint
from random import seed
import os
import time

from Class1 import Grille
from Class2 import Joueur
from Recur import Revele
import IA_console as IA
def verification(Tab):
    """
    Permet de vérifier si le tableau est bien crée avec 50 bombes.
    Arguement :
        Tab : Argument de type Grille.
    Return : rien .
    Print: affiche le nombre de bombes dans la console.
    """
    compteur:int = 0
    for i in range(Tab.taille):
        for j in range(Tab.taille):
            if (Tab.tableau_jeu[i][j] == -1):
                compteur = compteur + 1
    print(compteur)    


def guess(Objet:Grille):
    """
    La grille prise en argument est celle coté joueur.
    """
    x:int = 16
    y:int = 16
    while (x > 15) or (x < 0):
        x = int(input("Donnez la Ligne ou vous voulez cliquer (jusqu'à 15):"))
    while (y > 15) or (y < 0):
        y = int(input("Donnez la Colonne ou vous voulez cliquer (jusqu'à 15):"))
    while deja_pris(Objet,x,y):
        print("Case déjà cliquée")
        x:int = 16
        y:int = 16
        while (x > 15) or (x < 0):
            x = int(input("Donnez la Ligne ou vous voulez cliquer (jusqu'à 15):"))
        
        while (y > 15) or (y < 0):
            y = int(input("Donnez la Colonne ou vous voulez cliquer (jusqu'à 15):"))

    return x,y

def deja_pris(Objet:Grille,x,y):
    """voir si la case est prise
    Objet : Grille coté joueur
    
    Return booléen"""
    if Objet.tableau_jeu[x][y] == ".":
        return False
    else:
        return True

def separation():
    """séparation dans la console"""
    print("-"*100)

def main():
    """
    Lancement du Programme principal.
    """
    choix:int = int(input("Choix du mode : \n -> 0 pour un tableau généré aléatoirement \n -> 1 Pour un tableau venant d'un fichier \n -> 10 Pour faire 50 parties et voir quelle ia gagnera \n Votre choix : "))
    if (choix == 0):
        Tableau_Reponse = Grille()
        Tableau_Reponse.tableau_mine_init()
        Tableau_Joueur = Grille()
        Tableau_Joueur.tableau_joueur()
        Tableau_Reponse.stockage_tableau()
        mdj(Tableau_Reponse,Tableau_Joueur)
    elif (choix == 1):
        Tableau_Reponse = Grille()
        Tableau_Reponse.tableau_chargement()
        separation()
        Tableau_Joueur = Grille()
        Tableau_Joueur.tableau_joueur()
        Tableau_Reponse.stockage_tableau()
        mdj(Tableau_Reponse,Tableau_Joueur)
    elif (choix == 10):
        Concours()
    else:
        print("Vous avez mis un choix inexistant. Réessayez.")
        main()
        return 1

def mdj(Tableau_Reponse,Tableau_Joueur):
    choix = int(input("Choix de joueurs : \n -> 0 Pour 2 joueurs\n -> 1 Pour Joueur et IA\n -> 2 Pour 2 IA \n ->Votre choix : "))
    if (choix == 0):
        DeuxJoueurs(Tableau_Reponse,Tableau_Joueur)
    elif (choix == 1):
        JoueuretIA(Tableau_Reponse,Tableau_Joueur)
    elif (choix == 2):
        deuxIA(Tableau_Reponse,Tableau_Joueur)
    else:
        print("Vous avez mis un choix inexistant. Réessayez.")
        mdj(Tableau_Reponse,Tableau_Joueur)
        return 1
    
def DeuxJoueurs(Tableau_Reponse,Tableau_Joueur):
    Joueur1 = Joueur()
    Joueur2 = Joueur()
    if (randint(0,1) == 1):
        Joueur1.changement_joueur(Joueur2)
    else:
        Joueur2.changement_joueur(Joueur1)
        
    while (Tableau_Reponse.bombes != 0) and (Joueur1.score <= 25) and (Joueur2.score <= 25):
        if (Joueur1.tour == True):
            print("Au joueur 1 de jouer.")
            temp = Joueur1.score
            Nb_tour = 0
            while (temp < Joueur1.score) or (Nb_tour == 0):
                Tableau_Joueur.affichage()
                separation()
                if temp < Joueur1.score :
                    temp = Joueur1.score
                    print("Joueur1,encore a toi.")
                x,y = guess(Tableau_Joueur)
                Revele(Tableau_Reponse,Tableau_Joueur,x,y,Joueur1)
                Nb_tour = Nb_tour + 1
                print(f"Voici les scores: \n->Joueur1 : {Joueur1.score}\n->Joueur2 : {Joueur2.score}")
            Joueur1.changement_joueur(Joueur2)
        else:
            print("Au joueur 2 de jouer.")
            temp = Joueur2.score
            Nb_tour = 0
            while (temp < Joueur2.score) or (Nb_tour == 0):
                Tableau_Joueur.affichage()
                separation()
                if temp < Joueur2.score :
                    temp = Joueur2.score
                    print("Joueur 2, encore a toi.")
                x,y = guess(Tableau_Joueur)
                Revele(Tableau_Reponse,Tableau_Joueur,x,y,Joueur2)
                Nb_tour = Nb_tour + 1
                print(f"Voici les scores: \n->Joueur1 : {Joueur1.score}\n->Joueur2 : {Joueur2.score}")
            Joueur1.changement_joueur(Joueur2)
        
        print("Fin du jeu!\nVoici le gagnant... : ")
        if (Joueur1.score > 25) :
            print("Victoire du Joueur 1")
        elif (Joueur2.score > 25) :
            print("Victoire du Joueur 2")
        else:
            print("égalité!")
        #choix = int(input("Voulez vous stocker le Tableau de jeu entier? \1->Oui\n2->Non\nVotre choix : "))
        #if (choix == 1):
            #Tableau_Reponse.stockage_tableau()
        print("Merci d'avoir joué!")
    
def JoueuretIA(Tableau_Reponse,Tableau_Joueur):
    """Programme qui permet de jouer avec notre ia."""
    Joueur1 = Joueur()
    Profil_IA = Joueur()
    Grille_de_IA = IA.Grille_IA()
    if (randint(0,1) == 1):
        Joueur1.changement_joueur(Profil_IA)
    else:
        Profil_IA.changement_joueur(Joueur1)
    while (Tableau_Reponse.bombes != 0) and (Joueur1.score <= 25) and (Profil_IA.score <= 25):
        if (Joueur1.tour == True):
                print("Au joueur 1 de jouer.")
                temp = Joueur1.score
                Nb_tour = 0
                while (temp < Joueur1.score) or (Nb_tour == 0):
                    Tableau_Joueur.affichage()
                    separation()
                    if temp < Joueur1.score :
                        temp = Joueur1.score
                        print("Joueur1,encore a toi.")
                    x,y = guess(Tableau_Joueur)
                    Revele(Tableau_Reponse,Tableau_Joueur,x,y,Joueur1)
                    Nb_tour = Nb_tour + 1
                print(f"Voici les scores: \n->Joueur1 : {Joueur1.score}\n->IA : {Profil_IA.score}")
                Joueur1.changement_joueur(Profil_IA)
        else:
            print("A l'IA de jouer")
            temp = Profil_IA.score
            Nb_tour = 0
            while (temp < Profil_IA.score) or (Nb_tour == 0):
                Grille_de_IA.Play(Tableau_Joueur)
                Tableau_Joueur.affichage()
                separation()
                if temp < Profil_IA.score :
                    temp = Profil_IA.score
                if len(Grille_de_IA.case_a_jouer) > 0:
                    x = Grille_de_IA.case_a_jouer[0][0]
                    y = Grille_de_IA.case_a_jouer[0][1]
                else:
                    x = Grille_de_IA.case_probas[0][0]
                    y = Grille_de_IA.case_probas[0][1]
                Revele(Tableau_Reponse,Tableau_Joueur,x,y,Profil_IA)
                Nb_tour = Nb_tour + 1
                print(f"x choisi par l'ia : {x}, y choisi par l'ia : {y}")
                attente = str(input(""))
            print(f"Voici les scores: \n->Joueur1 : {Joueur1.score}\n->IA : {Profil_IA.score}")
            Profil_IA.changement_joueur(Joueur1)
    print("Fin du jeu!\nVoici le gagnant... : ")
    if (Joueur1.score > 25) :
        print(f"Victoire du Joueur 1 avec {Joueur1.score} Bombes trouvées.\nL'IA en avait {Profil_IA.score}")
    elif (Profil_IA.score > 25) :
        print(f"Victoire de l'IA avec {Profil_IA.score} Bombes trouvées\n Le joueur 2 en avait {Joueur1.score}")
    else:
        print("égalité!")
    #choix = int(input("Voulez vous stocker le Tableau de jeu entier? \1->Oui\n2->Non\nVotre choix : "))
    #if (choix == 1):
        #Tableau_Reponse.stockage_tableau()
    print("Merci d'avoir joué!")    


def deuxIA(Tableau_Reponse,Tableau_Joueur):
    Tableau_Reponse.stockage_tableau()
    Profil_IA_2 = Joueur()
    Profil_IA_1 = Joueur()
    Grille_de_IA_1 = IA.Grille_IA()
    Grille_de_IA_2 = IA.Grille_IA()
    if (randint(0,1) == 1):
        Profil_IA_2.changement_joueur(Profil_IA_1)
    else:
        Profil_IA_1.changement_joueur(Profil_IA_2 )
    while (Tableau_Reponse.bombes != 0) and (Profil_IA_1.score <= 25) and (Profil_IA_2.score <= 25):
        if (Profil_IA_1.tour == True):
                print("A l'IA 1 de jouer")
                temp = Profil_IA_1.score
                Nb_tour = 0
                while (temp < Profil_IA_1.score) or (Nb_tour == 0):
                    Grille_de_IA_1.Play(Tableau_Joueur)
                    Tableau_Joueur.affichage()
                    separation()
                    if temp < Profil_IA_1.score :
                        temp = Profil_IA_1.score
                    if len(Grille_de_IA_1.case_a_jouer) > 0:
                        x = Grille_de_IA_1.case_a_jouer[0][0]
                        y = Grille_de_IA_1.case_a_jouer[0][1]
                    else:
                        x = Grille_de_IA_1.case_probas[0][0]
                        y = Grille_de_IA_1.case_probas[0][1]
                    Revele(Tableau_Reponse,Tableau_Joueur,x,y,Profil_IA_1)
                    Nb_tour = Nb_tour + 1
                    print(f"x choisi par l'ia : {x}, y choisi par l'ia : {y}")
                    attente = str(input(""))
                print(f"Voici les scores: \n->IA 2 : {Profil_IA_2.score}\n->IA 1: {Profil_IA_1.score}")
                Profil_IA_1.changement_joueur(Profil_IA_2)
        else:
            print("A l'IA de jouer")
            temp = Profil_IA_2.score
            Nb_tour = 0
            while (temp < Profil_IA_2.score) or (Nb_tour == 0):
                Grille_de_IA_2.Play(Tableau_Joueur)
                Tableau_Joueur.affichage()
                separation()
                if temp < Profil_IA_2.score :
                    temp = Profil_IA_2.score
                if len(Grille_de_IA_2.case_a_jouer) > 0:
                    x = Grille_de_IA_2.case_a_jouer[0][0]
                    y = Grille_de_IA_2.case_a_jouer[0][1]
                else:
                    x = Grille_de_IA_2.case_probas[0][0]
                    y = Grille_de_IA_2.case_probas[0][1]
                Revele(Tableau_Reponse,Tableau_Joueur,x,y,Profil_IA_2)
                Nb_tour = Nb_tour + 1
                print(f"x choisi par l'ia : {x}, y choisi par l'ia : {y}")
                attente = str(input(""))
            print(f"Voici les scores: \n->IA 2 : {Profil_IA_2.score}\n->IA 1: {Profil_IA_1.score}")
            Profil_IA_2.changement_joueur(Profil_IA_1)
    print("Fin du jeu!\nVoici le gagnant... : ")
    if (Profil_IA_2.score > 25) :
        print(f"Victoire de l'IA 2 avec {Profil_IA_2.score} Bombes trouvées.\nL'IA 1 en avait {Profil_IA_1.score}")
    elif (Profil_IA_1.score > 25) :
        print(f"Victoire de l'IA 1  avec {Profil_IA_1.score} Bombes trouvées\n L'IA 2 en avait {Profil_IA_2.score}")
    else:
        print("égalité!")
    #choix = int(input("Voulez vous stocker le Tableau de jeu entier? \1->Oui\n2->Non\nVotre choix : "))
    #if (choix == 1):
        #Tableau_Reponse.stockage_tableau()
    print("Merci d'avoir joué!")

def Concours():
    score_IA1 = 0 # IA PERSO
    score_IA2 = 0 # AUTRE IA
    for i in range(50): #Nombre de parties jouées;
        print(f"Partie numéro {i+1}")
        Tableau_Reponse = Grille()
        Tableau_Reponse.tableau_mine_init()
        Tableau_Joueur = Grille()
        Tableau_Joueur.tableau_joueur()
        score_IA1, score_IA2 = Concours_jeu(Tableau_Reponse,Tableau_Joueur,score_IA1,score_IA2)
        
    print(f"Voici les scores :\nPour l'ia extérieure, elle a gagnée {score_IA2}\nPour notre IA : {score_IA1} ")


def Concours_jeu(Tableau_Reponse,Tableau_Joueur,score_IA1,score_IA2):
    seed()
    #IA PERSO
    Profil_IA_1 = Joueur() 
    Grille_de_IA_1 = IA.Grille_IA()
    #AUTRE IA
    Profil_IA_2 = Joueur()
    Grille_de_IA_2 = IA.Grille_IA()

    if (randint(0,1) == 1):
        Profil_IA_2.changement_joueur(Profil_IA_1)#IA PERSO
    else:
        Profil_IA_1.changement_joueur(Profil_IA_2)#AUTRE IA

    while (Tableau_Reponse.bombes != 0) and (Profil_IA_1.score <= 25) and (Profil_IA_2.score <= 25):
        if (Profil_IA_1.tour == True):
            temp = Profil_IA_1.score
            Nb_tour = 0
            while (temp < Profil_IA_1.score) or (Nb_tour == 0):
                Grille_de_IA_1.Play(Tableau_Joueur)
                if temp < Profil_IA_1.score :
                    temp = Profil_IA_1.score
                if len(Grille_de_IA_1.case_a_jouer) > 0:
                    x = Grille_de_IA_1.case_a_jouer[0][0]
                    y = Grille_de_IA_1.case_a_jouer[0][1]
                else:
                    x = Grille_de_IA_1.case_probas[0][0]
                    y = Grille_de_IA_1.case_probas[0][1]
                Revele(Tableau_Reponse,Tableau_Joueur,x,y,Profil_IA_1)
                Nb_tour = Nb_tour + 1
            Profil_IA_1.changement_joueur(Profil_IA_2)
        else:
            temp = Profil_IA_2.score
            Nb_tour = 0
            while (temp < Profil_IA_2.score) or (Nb_tour == 0):
                Grille_de_IA_2.Play(Tableau_Joueur)
                if temp < Profil_IA_2.score :
                    temp = Profil_IA_2.score
                if len(Grille_de_IA_2.case_a_jouer) > 0:
                    x = Grille_de_IA_2.case_a_jouer[0][0]
                    y = Grille_de_IA_2.case_a_jouer[0][1]
                else:
                    x = Grille_de_IA_2.case_probas[0][0]
                    y = Grille_de_IA_2.case_probas[0][1]
                Revele(Tableau_Reponse,Tableau_Joueur,x,y,Profil_IA_2)
                Nb_tour = Nb_tour + 1
            Profil_IA_2.changement_joueur(Profil_IA_1)
    if (Profil_IA_2.score > 25) :
        return score_IA1, score_IA2 + 1
    elif (Profil_IA_1.score > 25) :
        return score_IA1 + 1, score_IA2 
    else:
        return score_IA1, score_IA2
main()
