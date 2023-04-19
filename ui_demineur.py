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
        self.grille_d = self.demineur.grille
        self.liste_bouton = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Démineur')
        tabgrille = self.demineur.grille_non_visible
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
        pos:tuple
        for elem in self.liste_bouton:
            if button == elem[1]:
                pos = elem[0]
        print(pos)


        

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Minesweeper()
    sys.exit(app.exec_())

    
