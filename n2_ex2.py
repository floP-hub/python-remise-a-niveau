# fonctions : factorielle(nombre)
# math : factoriel, noté n!, est le produit de tous les entiers, de 1 jusqu'au nombre n
# n doit être un entier naturel
# 0! = 1
#1) avec boucle :
def factorielle_boucle(nombre) :
    factoriel = 1
    if nombre == 0 : 
        return factoriel
    elif nombre > 0 :
        for i in range (1,nombre+1) :
            factoriel = factoriel * i
        return factoriel
    #traitement simplifié d'une entrée incorrecte :
    else :
        return -1 

#2) avec récursivité : la fonction doit s'appeler elle même, avec une condition d'arrêt

def factorielle_recursive (nombre) :
    # 0! = 1 : condition d'arrêt (cas de base)
    if nombre == 0 :
        return 1
    # Pour tout entier n>0, n! = (n−1)!× n : appel récursif
    else :
        return nombre * factorielle_recursive(nombre-1)

#utilisation des fonctions :
nb = int(float(input("saisissez un entier positif ou nul : ")))
print(f"par calcul en boucle, le factoriel du nombre est : {factorielle_boucle(nb)}")
print(f"par calcul récursif, le factoriel du nombre est : {factorielle_recursive(nb)}")