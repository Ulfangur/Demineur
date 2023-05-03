from Class1 import Grille
class fonction:
    def __init__()
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

    def probas(self,a,b,nb_bombes_reste):
        """(Appliqué si on a pas le nombre précis)
            Programme : Donne un couple (x,y,probabilité,nombre de bombes ) pour chacun des cas de vide."""  
        voisin = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,1),(1,0)]
        for x,y in voisin:
            if ((a + x < 16 and a + x > -1) and (b + y < 16 and b + y > -1)):
                if (self.tableau_jeu[a + x][b + y] == "."):
                    self.case_probas.append((a+x,b+y,1/nb_bombes_reste,nb_bombes_reste))       
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