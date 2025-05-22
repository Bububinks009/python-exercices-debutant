# Supprimer les doublons d’une liste sans utiliser set().
# Cette methode ne supprime pas directement les doublons de la liste mais crée une nuvelle liste et y ajoute les éléments de la principale liste en evitant de prendre deux fois le meme elements dans la liste

l = [8,8,9,7,5,1,6,1,8,5,2,3,7,4,6,9,4,7,5,3,8,1,3,8,1,3,0,1,9,1,2,9,1] # creation d une liste l contenant des entier
m = [] # creation d une liste vide m pour y ajouter les element
for i in l: # pour tout les elements i de la liste l
    if i not in m: # si i n appartient pas a la liste m
        m.append(i) # ajouter i a la liste m
        m.sort() # cette ligne est juste un petit ajout facultatif , donc qui peut etre effacé sans vraiment impacter la compilation. Elle sert juste a trier la liste m qui sera afficher par ordre croissants
print(m) # afficher la liste m