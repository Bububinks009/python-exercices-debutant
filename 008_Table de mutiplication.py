# Écrire un programme qui affiche la table de multiplication d’un nombre donné.

t = 0  # initialisation de la variable t dans laquelle sera stocker les resultat des calcul de la table de multiplication
i = 0  # initialisation de la variable i qui stockera les indices de calcul de la table de multiplication
n = int(input("Entrer un nombre entier :"))  # demande a l utilisateur d entrer un entier
while i<=12:  # tant que i est inferieur ou egal a 12
    t = n*i  # calculé n fois i et affecter le resultat a t
    print( n,"*",i,"=", t)  # afficher n*i=t
    i+=1  # ajouter 1 a i et reprendre l operation
