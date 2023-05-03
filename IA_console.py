from Class1 import Grille

class Grille_IA(Grille):
    def __init__(self):
        self.tableau_jeu = self.tableau_joueur()
    def update(self,other):
        """Other doit être la grille vu par les joueurs."""
        for i in range(16):
            for j in range(16):
                if (other.tableau_jeu[i][j] != ".") and (self.tableau_jeu[i][j] == "." or self.tableau_jeu[i][j] == "\\") :
                    self.tableau_jeu[i][j] = other.tableau_jeu[i][j]
        