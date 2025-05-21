# Écrire un jeu de << devine le nombre >> (entre 1 et 100).

import random  # importe la bibliotheque random qui genere des nombre aleatoire compris entre des intervalles definies
n = random.randint(1,100)  # genrer le nombre n aleatoire
m = 0  # initialise m a zero
essais = 0  # initialise le nombre d essais a zero
while n != m: # tant que n different de m 
    m = int(input( " Entrer un entier compris entre 1 et 100 :"))  # demande a l utilisateur d entrer un nombre m compris entre 1 et 100
    essais += 1  # ajoute 1 a la valeur de essais a chaque tour realiser
    if m < n :   # si m inferieur a n
        print( m , " est inferieur au nombre. ")  # afficher m inferieur au nombre
    elif m > n :  # sinon si m superieur au nombre 
        print( m , " est superieur au nombre. ")  # afficher m superieur au nombre
    else:  # sinon 
        print( m , " est juste. ")  # afficher m est juste

print(" Essais = " , essais )  # afficher Essais = essais
