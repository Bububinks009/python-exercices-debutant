#  Vérifier si une chaîne est un palindrome.

t = input("Entrer une chaine de caractere :") # demande a l utilisateur d entrer une chaine et la stocke dans t
i = t[::-1]  # inverse la chaine stocker dans t et la stocke dans i
if t == i :  # verifi si t egale a i , si c est vrai
    print( t , " est un palindrome ")  # affiche t est un palindrome
else:  # sinon
    print( t , " n'est pas un palindrome ")  # affiche t n est pas un palindrome
