import random
# 1) input et print
print("votre prénom : ")
prenom = input()
print ("Bonjour, "+prenom+" !")
#le prompt peut être un paramètre dans input :
couleur = input("votre couleur préférée : ")
#le print d'un f-string : 
print (f"Ah, vous aimez la couleur {couleur}")

print("*******")

# 2) print d'un calcul dans une boucle
# convertir la saisie en nombre entier :
nombre = int(float(input("saisissez un nombre :")))
print ("voici sa table de multiplication :")
for i in range (1,11):
    mult = nombre * i
    print(f"{nombre} * {i} = {mult} ")

print("*******")

# 3)
#random.randint(borne inf, borne sup) : génère un entier
nb = random.randint(1,100)
print("trouvez un nombre entre 1 et 100")
trouve=False
while not trouve :
    choix = int(float(input("saisissez un nombre entre 1 et 100 : ")))
    if choix == nb :
        trouve=True
        print("trouvé ! bravo !")
    elif choix < nb :
        print("plus grand")
    elif choix > nb :
        print("plus petit")
    else :
        print("erreur, recommencez")
