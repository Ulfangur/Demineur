from random import randint
import os

from Class1 import Grille
from Class2 import Joueur
from Recur import Revele
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
    if Objet.tableau_jeu[x][y] == ".":
        return False
    else:
        return True

def separation():
    print("-"*100)

def main():
    choix:int = int(input("Choix du mode : \n -> 0 pour un tableau généré aléatoirement \n -> 1 Pour un tableau venant d'un fichier \n Votre choix : "))
    if (choix == 0):
        Tableau_Reponse = Grille()
        Tableau_Reponse.tableau_mine_init()
        Tableau_Reponse.affichage()
        separation()
        Tableau_Joueur = Grille()
        Tableau_Joueur.tableau_joueur()
    elif (choix == 1):
        Tableau_Reponse = Grille()
        Tableau_Reponse.tableau_chargement()
        Tableau_Reponse.affichage()
        separation()
        Tableau_Joueur = Grille()
        Tableau_Joueur.tableau_joueur()
    else:
        print("Vous avez mis un choix inexistant. Réessayez.")
        main()
        return 1
    Tableau_Reponse.stockage_tableau()
    Joueur1 = Joueur()
    Joueur2 = Joueur()
    if (randint(0,1) == 1):
        Joueur1.changement_joueur(Joueur2)
    else:
        Joueur2.changement_joueur(Joueur1)
    
    while (Tableau_Reponse.bombes != 0) or (Joueur1 < 25) or (Joueur2 < 25):
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
    if (Joueur1.bombe > 25) :
        print("Victoire du Joueur 1")
    elif (Joueur2.bombe > 25) :
        print("Victoire du Joueur 2")
    else:
        print("égalité!")
    #choix = int(input("Voulez vous stocker le Tableau de jeu entier? \1->Oui\n2->Non\nVotre choix : "))
    #if (choix == 1):
        #Tableau_Reponse.stockage_tableau()
    print("Merci d'avoir joué!")
main()