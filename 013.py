# Trier une liste sans utiliser la fonction sort().

l = [8,2,7,24,3,8,6,8,67,1,73,1,6,8,60,3,9,2,3,6,7,1,3,6,81,36,3,6,1,5,76,5,7,62] # creation d une liste l avec des nombres désordonnées
n = len(l) # la foction len() compte le nombre d elements dans la liste l et la stocke dans la variable n

for i in range(n): # pour i allant de la position 0 a n
    for j in range(i+1, n): # pour j allant de la position 1 a n
        if l[i] > l[j]: # si l element a la position i est superieur a l element a la position j
            l[i], l[j] = l[j], l[i] # on remplace l[i] par l[j] et inversement

print("Liste triée :", l) # affiche la liste triée