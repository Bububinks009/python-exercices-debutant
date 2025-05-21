# Trouver le plus grand de 3 nombres donnés par l’utilisateur . 

n1 = float(input( " Entrer un nombre n1 : "))
n2 = float(input( " Entrer un nombre n2 : "))
n3 = float(input( " Entrer un nombre n3 : "))
if (n1>n2)&(n1>n3):
    print( " Le plus grand nombre est : " , n1)
elif (n2>n1)&(n2>n3):
    print( " Le plus grand nombre est : " , n2)
else:
    print( " Le plus grand nombre est : " , n3)
