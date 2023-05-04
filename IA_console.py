from Class1 import Grille
import math
class Fraction:
    def __init__(self,x,y):
        self.numerateur = x
        self.denominateur = y
    def addition(self,other):
        """Other est un objet de type fraction"""
        self.numerateur = self.numerateur * other.denominateur + other.numerateur * self.denominateur
        self.denominateur = self.denominateur * other.denominateur
        self.reduire()
    def reduire(self):
        pgcd = math.gcd(self.numerateur,self.denominateur)
        self.numerateur = self.numerateur / pgcd
        self.denominateur = self.denominateur / pgcd
    def multiplier(self,other):
        """Other est un objet de type fraction"""
        self.numerateur = self.numerateur * other.numerateur
        self.denominateur = self.denominateur * other.denominateur
        self.reduire()
    def diviser(self,n):
        Temp = Fraction(1,n)
        self.multiplier(Temp)
    def flottant(self):
        return self.numerateur / self.denominateur

class Grille_IA(Grille):
    def __init__(self):
        self.tableau_joueur()
        self.case_a_jouer = []
        self.case_probas = []

    def update(self,other):
        """Other doit être la grille vu par les joueurs."""
        for i in range(16):
            for j in range(16):
                if (other.tableau_jeu[i][j] != ".") and (self.tableau_jeu[i][j] == "." or self.tableau_jeu[i][j] == "\\") :
                    self.tableau_jeu[i][j] = other.tableau_jeu[i][j]
        self.affichage()
    
    def autour(self):
        voisin = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,1),(1,0)]
        for i in range(16):
            for j in range(16):
                value = self.tableau_jeu[i][j]
                if ((value != "." or value != "\\") or value != "B"):
                    for x,y in voisin:
                        if ((i + x < 16 and i + x > -1) and (j + y < 16 and j + y > -1)):
                            if self.tableau_jeu[i + x][j + y] == "B":
                                value = value -1
                    if value == 0:
                        self.voisins(i,j)
    
    def voisins(self,a,b):
        voisin = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,1),(1,0)]
        for x,y in voisin :
            if ((a + x < 16 and a + x > -1) and (b + y < 16 and b + y > -1)):
                if (self.tableau_jeu[a + x][b + y] == "."):
                    self.tableau_jeu[a + x][b + y] = "\\"
    
    def jouer(self):
        for i in range(16):
            for j in range(16):
                if ((self.tableau_jeu[i][j] != 0) and (self.tableau_jeu[i][j] != ".")) : 
                    nb_case_vide = self.nombre_vide(i,j)
                    nb_bombes = self.nombre_bombes(i,j)
                    bombes_restantes = self.tableau_jeu[i][j]- nb_bombes
                    if (bombes_restantes == nb_case_vide) :
                        self.coord_vide(i,j)
                    else:
                        self.probas(i,j,bombes_restantes)
        #Réduction du tableaux de probas :
        self.reduction_probas()

    def probas(self,a,b,nb_bombes_reste):
        """(Appliqué si on a pas le nombre précis)
            Programme : Donne un couple (x,y,probabilité,nombre de bombes ) pour chacun des cas de vide."""  
        voisin = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,1),(1,0)]
        for x,y in voisin:
            if ((a + x < 16 and a + x > -1) and (b + y < 16 and b + y > -1)):
                if (self.tableau_jeu[a + x][b + y] == "."):
                    Temp = Fraction(1,nb_bombes_reste)
                    self.case_probas.append((a+x,b+y,Temp,nb_bombes_reste))  

    def reduction_probas(self):
        """
        On utilise case_probas réduire les paires.
        chaque tuple est de la forme suivante:
        ( Coordonnées I, Coordonnées J, Fraction de probabilité de type Fraction,Nb_de bombes )
        Après le programme, chaque Tuple sera de cette forme : 
        ( Coordonnées I, Coordonnées J, Fraction de probabilité de type Fraction,nombre de cases qui ammènent vers cet endroit)
        """
        # D'abord un tri par coordonnées x :
        self.tri_proba()
        Tableau = []
        #Dans_Tableau vérifie si les coordonnées sont déja dans le tableau ou pas, si True alors elles y sont deja
        Dans_Tableau = False
        for i in range(len(self.case_probas)):
            Dans_Tableau = False
            for j in range(len(Tableau)):
                if ((self.case_probas[i][0] == Tableau[j][0]) and (self.case_probas[i][1] == Tableau[j][1])):
                    Dans_Tableau = True
                    Dans = j
            if not Dans_Tableau:
                paires = (self.case_probas[i][0],self.case_probas[i][1],self.case_probas[i][2],1)
                Tableau.append(paires)
            else:
                Tableau[Dans][3] = Tableau[Dans][3] + 1
                Tableau[Dans][2].addition(self.case_probas[i][2])
        #Calcul Probas et tri en fonction des probas:
        for e in Tableau :
            e[2].diviser(e[3])
        self.tri_fonction_probas()
                
        
    def tri_fonction_probas(self):
        """Tri en fonction des probas
            Chaque tuple est de la forme (proba, indice dans le tableau case_probas)
            Ce qui permettra de tout refaire ensuite."""
        #On commence par créer un tableau de tuples, avec proba et places dans le tableau case_probas
        Tableau = []
        for i in range(len(self.case_probas)):
            paire = (self.case_probas[i][2].flottant(),i)
            Tableau.append(paire)

        #Tri double : 

        for i in range(len(Tableau)//2):
            maxi = len(Tableau) - i - 1
            max_i = len(Tableau) - i - 1
            mini = i
            for j in range(i+1,len(self.case_probas)-i):
                if Tableau[mini][0] > Tableau[j][0]:
                    mini = j
                if Tableau[maxi][0] < Tableau[j][0]:
                    maxi = j
            # Minimum
            temp = Tableau[i][0]
            Tableau[i][0] = Tableau[mini][0]
            Tableau[mini][0] = temp
            # Maximum 
            temp = Tableau[maxi][0]
            Tableau[maxi][0] = Tableau[max_i][0]
            Tableau[max_i][0] = temp
        #Changement du sens du tableau, on en recréer un pour le remplacer ensuite : 

        Tableau_final = []
        for i in range(len(Tableau)):
            Tableau_final.append(self.case_probas[Tableau[i][1]])
        self.case_probas = Tableau_final

    def tri_proba(self):
        """Tri en fonction des Coordonées"""
        for i in range(len(self.case_probas)//2):
            maxi = len(self.case_probas) - i - 1
            max_i = len(self.case_probas) - i - 1
            mini = i
            
            for j in range(i+1,len(self.case_probas)-i):
                if self.case_probas[mini][0] > self.case_probas[j][0]:
                    mini = j
                if self.case_probas[maxi][0] < self.case_probas[j][0]:
                    maxi = j
            # Minimum
            temp = self.case_probas[i][0]
            self.case_probas[i][0] = self.case_probas[mini][0]
            self.case_probas[mini][0] = temp
            # Maximum 
            temp = self.case_probas[maxi][0]
            self.case_probas[maxi][0] = self.case_probas[max_i][0]
            self.case_probas[max_i][0] = temp

    def coord_vide(self,a,b):
        """(Appliqué si Le nombre de case vide est le même que le nombre restant de bombes a un point x y)
            Programme qui donne les coordonnées des cases vides dans case_a_jouer"""
        voisin = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,1),(1,0)]
        for x,y in voisin:
            if ((a + x < 16 and a + x > -1) and (b + y < 16 and b + y > -1)):
                if (self.tableau_jeu[a + x][b + y] == "."):
                    self.case_a_jouer.append((a+x,b+y))

    def nombre_vide(self,a,b):
        voisin = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,1),(1,0)]
        compteur = 0
        for x,y in voisin:
            if ((a + x < 16 and a + x > -1) and (b + y < 16 and b + y > -1)):
                if (self.tableau_jeu[a + x][b + y] == "."):
                    compteur = compteur + 1
        return compteur
    
    def nombre_bombes(self,a,b):
        voisin = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,1),(1,0)]
        compteur = 0
        for x,y in voisin:
            if ((a + x < 16 and a + x > -1) and (b + y < 16 and b + y > -1)):
                if (self.tableau_jeu[a + x][b + y] == "B"):
                    compteur = compteur + 1
        return compteur
    
    def Play(self):
        