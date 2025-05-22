# Écrire un dictionnaire qui contient les notes de plusieurs étudiants, puis afficher la moyenne de chacun.

# creation du dictionnaire de notes
Notes = {
    " Beracka" : [ 17,18,15,20,14],
    " Jérémie" : [ 16,17,14,19,17],
    " Lumiere" : [ 8,13,11,17,15],
    " Généreux" : [ 12,16,10,15,18] 
}
# Calcul de la moyenne de chaque étudiant
for i in Notes: # pour chaque elements i du dictionnaire Notes
    t = sum(Notes[i])  # la fonction sum() fait la somme de toutes les notes de chaque liste et affecte le resultat a t
    n = len(Notes[i])  # la fonction len() fait le decompte du nombre de notes dans chaque liste de notes et affecte le resultat a n 
    m = t / n  # Calcul de la moyenne
    print(f"{i} a une moyenne de {m:.2f}") # affiche la moyenne