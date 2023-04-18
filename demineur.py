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
print("------------------------------------")
Reponse.tableau_mine_init()
Reponse.affichage()
print("------------------------------------")
Reponse2 = Grille.Grille()
#Reponse2.tableau_chargement()
Reponse2.affichage()
print("------------------------------------")
#verification(Test)

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
    if Objet.tableau_jeu[x][y] == 0:
        return False
    else:
        return True

#temp1,temp2 = guess(Reponse2)
#print(type(temp1),temp1,type(temp2),temp2)