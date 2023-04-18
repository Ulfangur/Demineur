from random import randint
import Class1 as Grille
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


Reponse = Grille.Grille()
Reponse.affichage()
print("------------------------------------")
Reponse.tableau_mine_init()
Reponse.affichage()


#verification(Test)


