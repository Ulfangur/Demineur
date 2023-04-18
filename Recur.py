def Revele(Grille_Reponse,Grille_Joueur,x,y,Joueur):
    """
    il faudra changer le Joueur a la fin de son tour en comparant le nombre de bombes avant et après ce programme
    """
    if (Grille_Reponse.tableau_jeu[x][y] != 0):
        Grille_Joueur.tableau_jeu[x][y] = Grille_Reponse.tableau_jeu[x][y]
        if (Grille_Reponse.tableau_jeu[x][y] == -1):
            Joueur.bombe()

    else:
        Grille_Joueur.tableau_jeu[x][y] = Grille_Reponse.tableau_jeu[x][y]
        if (x==0):
            if (y==0):
                for i in range(2):
                    for j in range(2):
                        if i==0 and j==0:
                            ne_fais_rien = 0
                        else:
                            Revele(Grille_Reponse,Grille_Joueur,x+i,y+j)
            elif (y == Grille_Joueur.taille-1):
                for i in range(2):
                    for j in range(-1,1):
                        if i==0 and j==0:
                            ne_fais_rien = 0
                        else:
                            Revele(Grille_Reponse,Grille_Joueur,x+i,y+j)
            else:
                for i in range(0,2):
                    for j in range(-1,2):
                        if i==0 and j==0:
                            ne_fais_rien = 0
                        else:
                            Revele(Grille_Reponse,Grille_Joueur,x+i,y+j)
        elif (x == Grille_Joueur.taille-1):
            if (y==0):
                pass
            elif(y == Grille_Joueur.taille-1):
                pass
            else:
                for i in range(-1,1):
                    for j in range(-1,2):
                        if i==0 and j==0:
                            ne_fais_rien = 0
                        else:
                            Revele(Grille_Reponse,Grille_Joueur,x+i,y+j)
        elif (y==0):
            pass
        elif (y == Grille_Joueur.taille-1):
            pass
        else:
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    if i == 0 and j == 0:
                        ne_fais_rien = 0
                    else:
                        if Grille_Joueur.tableau_jeu[x+i][y+j] ==".":
                            Revele(Grille_Reponse,Grille_Joueur,x+i,y+j)

            
