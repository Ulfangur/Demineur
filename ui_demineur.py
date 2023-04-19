import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import QSize
from grille_youssef import Demineur

class Minesweeper(QWidget):
    def __init__(self, lignes=16, colonnes=16):
        super().__init__()
        self.lignes = lignes
        self.colonnes = colonnes
        self.demineur = Demineur()
        self.grille_non_visible = self.demineur.grille_non_visible
        self.grille_visible = self.demineur.grille
        self.liste_bouton = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Démineur')
        tabgrille = self.grille_non_visible
        grille = QGridLayout()
        self.setLayout(grille)
        for lignes in range(self.lignes):
            for colonnes in range(self.colonnes):
                button = QPushButton()
                button.setFixedSize(QSize(30, 30))
                valeur = str(tabgrille[lignes][colonnes])
                if valeur == "-1":
                    valeur = "*"
                button.setText(valeur)
                self.liste_bouton.append(((lignes,colonnes),button))
                self.layout().addWidget(button, lignes, colonnes)
        
        for button in self.liste_bouton:
            button[1].clicked.connect(self.on_button_clicked)

        self.show()
    
    def on_button_clicked(self):
        """
        Test des boutons quand ils sont cliqués
        Affiche la position dans self.grille dans la classe Demineur du bouton cliqué
        """
        button = self.sender()
        indice_a_modif = []
        pos:tuple
        for elem in self.liste_bouton:
            if button == elem[1]:
                pos = elem[0]
        indice_a_modif = self.demineur._cases_revele(pos[0], pos[1])
        for tuple_indice in indice_a_modif:
            for bouton in self.liste_bouton:
                if tuple_indice == bouton[0]:
                    valeur = str(self.grille_visible[tuple_indice[0]][tuple_indice[1]])
                    bouton[1].setText(valeur)
        


    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Minesweeper()
    sys.exit(app.exec_())

    
