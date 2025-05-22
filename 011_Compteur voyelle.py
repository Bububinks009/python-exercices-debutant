# Compter le nombre de voyelles dans une phrase.

n = 0 # initialise le compteur n  des voyelles a 0
v = "aeiouyAEIOUY" # variable v contenant les voyelles a verifier
p = input( " Entrer une phrase :") # demande a l utilisateur d entrer une phrase et la stocke dans p
for i in p: # pour chaque lettre i de la phrase p
    if i in v: # si la lettre i est dans v
        n +=1 # le compteur n fait +1 a sa valeur précédente
print( "Le nombre de voyelles dans cette phrase est :" , n) # affiche le nombre total de voyelles dans la phrase
