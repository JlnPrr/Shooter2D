
# https://www.udemy.com/course/pygame-apprendre-python-facilement-par-le-developpement-de-jeux-video/learn/lecture/28114640#overview

# Créer une function qui affiche un sapin de type dynamique
# *
# **
# ***
# ****
"""
def Sapin(nb=1):
    while nb >= 1:
        print("*")
        nb -= 1                                         # Sapin(3) _= 1 =  3 étoiles


print(Sapin(3))

"""
# _____________


def Sapin(nb=1):
    nbStars = 1
    while nb >= 1:
        for i in range(1, nbStars+1):                   # +1 pr éviter deux fois 1 (1, 1) et faire que ça commence au moins à deux (1, 2)
            print("*", end="")                          # end pr empêcher le retour à la ligne
        print("")
        nb -= 1
        nbStars += 1


Sapin(5)                                               # On appelle la function

# Resultat:
# *
# **
# ***
# ****
# *****
