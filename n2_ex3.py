# fonctions : palindrome
# mot ou groupe de mots qui peut se lire de la même manière de gauche à droite ou de droite à gauche
# radar, kayak, été, ressasser, rotor, ici tôt
# il peut s'agir de noms propres (prénom, ville) : Bob, Anna, Natan, Otto, Laval
# le plus souvent, on ne tient pas compte des accents, ni des des tirets, espaces et signes de ponctuation (phrase) : 
# rêver, réifier, élu par cette crapule
# on distingue les palindromes à nombre impair de lettres, où une lettre centrale est pivot, de ceux à nombre pair.
# dans cet exercice, on s'en tient aux mots, et la seule modification consiste à mettre la casse à égalité

#utilisation de la fonction de l'exercice 1 :
def est_Pair(entier) :
    if (entier % 2) == 0 :
        return True
    else :
        return False
    
def palindrome (mot) :
    #lissage de la casse : passage de toutes les lettres en minuscule
    mot_lisse = mot.lower()
    nb_car = len (mot_lisse)
    retour = False
    #dernier indice de caractère
    z = nb_car - 1 
    #on ne s'occupe pas de la lettre pivot si le mot est impair
    if not est_Pair(nb_car) :
        nb_car = nb_car - 1  
    stop = int((nb_car / 2))
    for i in range (0, stop) :
        a = mot_lisse[i]
        b = mot_lisse[z-i]
        if not (a==b) :
            print(f"{a} à la pos {i} est différent de {b} à la pos {z-i}")
            return retour
    retour = True
    return retour

#utilisation de la fonction
mot_choisi=input("saisissez un mot palindrome : ")
if palindrome(mot_choisi) :
    print("c'est bien un palindrome !")
else :
    print ("ce n'est PAS un palindrome !")