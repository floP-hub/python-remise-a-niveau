#fonctions :
#def nom_fonction(liste de paramètres):
#      bloc d'instructions

#1) estPair() retourne True ou False
def est_Pair(entier) :
    if (entier % 2) == 0 :
        return True
    else :
        return False

#utilisation de la fonction :
encore = True
while encore :
    nombre = int(float(input("saisissez un nombre : ")))
    if est_Pair(nombre) :
        print (f"{nombre} est paire")
    else :
        print (f"{nombre} est impaire")
    saisie = input("tapez n'importe quelle lettre pour continuer ou stop pour arrêter : ")
    if saisie == "stop" :
        encore = False