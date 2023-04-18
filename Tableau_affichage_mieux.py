fic = open("Tableau_jeu.txt","r")
lignes = fic.readlines()
T =[[0 for i in range(16)]for j in range(16)]
bombe:bool = False
Ligne:int = 0
Colonne:int = 0 
for ligne in lignes : 
    for e in ligne:
        if not bombe :
            if e != " " and e !="\n":
                if e == "-":
                    T[Ligne][Colonne] = "B"
                    bombe = True
                    Colonne = Colonne + 1
                else:
                    T[Ligne][Colonne] = e
                    Colonne = Colonne + 1
        else:
            bombe = False
    Ligne = Ligne +1
    Colonne = 0
fic.close()
fic2 = open("Tableau_mieux.txt","w")
for i in range(16):
    for j in range(16):
        fic2.write(str(T[i][j]))
        fic2.write(" ")
    fic2.write("\n")
fic2.close()