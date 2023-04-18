class Joueur:
    def __init__(self):
        """
        self.jeu:
            True si le joueur doit jouer
            False sinon
        """
        self.tour:bool = False
        self.score:int = 0
    
    def bombe(self):
        self.score = self.score + 1
    
    def changement_joueur(self,other):
        if self.tour == False:
            self.tour = True
            other.tour = False
        else:
            self.tour = False
            other.tour = True