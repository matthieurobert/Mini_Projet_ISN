#il y a un problème il faut modifier le début car la valeur et la carte ne sont pas pareils sa veut dire que la valeur et l'image on deut paquets diff
from pygame.locals import *
def tirage_de_la_carte():
    from initpaquet import paquets
    import pygame


    pygame.init()
    valeur=int
    carte = paquets()[:1] #on tire une carte
    del paquets()[:1] #on l'enlève du paquet

    if carte==['as de ♠']:                                                       # si la carte est un 'as de ♠'
        card = pygame.image.load("cartes/as♠.png").convert()                     # alors on affiche la carte 2♠ du document cartes
        valeur=1
    if carte==['2 de ♠']:
        card = pygame.image.load("cartes/2♠.png").convert()                      # de même pour les autre cartes
        valeur=2
    if carte==['3 de ♠']:
        card = pygame.image.load("cartes/3♠.png").convert()
        valeur=2
    if carte==['4 de ♠']:
       card = pygame.image.load("cartes/4♠.png").convert()
       valeur=4
    if carte==['5 de ♠']:
        card = pygame.image.load("cartes/5♠.png").convert()
        valeur=5
    if carte==['6 de ♠']:
        card = pygame.image.load("cartes/6♠.png").convert()
        valeur=6
    if carte==['7 de ♠']:
        card = pygame.image.load("cartes/7♠.png").convert()
        valeur=7
    if carte==['8 de ♠']:
        card = pygame.image.load("cartes/8♠.png").convert()
        valeur=8
    if carte==['9 de ♠']:
        card = pygame.image.load("cartes/9♠.png").convert()
        valeur=9
    if carte==['10 de ♠']:
        card = pygame.image.load("cartes/10♠.png").convert()
        valeur=10
    if carte==['Valet de ♠']:
        card = pygame.image.load("cartes/J♠.png").convert()
        valeur=10
    if carte==['Dame de ♠']:
        card = pygame.image.load("cartes/Q♠.png").convert()
        valeur=10
    if carte==['Roi de ♠']:
        card = pygame.image.load("cartes/K♠.png").convert()
        valeur=10

    if carte==['as de ♣']:
        card = pygame.image.load("cartes/as♣.png").convert()
        valeur=1
    if carte==['2 de ♣']:
        card = pygame.image.load("cartes/2♣.png").convert()
        valeur=2
    if carte==['3 de ♣']:
        card = pygame.image.load("cartes/3♣.png").convert()
        valeur=3
    if carte==['4 de ♣']:
        card = pygame.image.load("cartes/4♣.png").convert()
        valeur=4
    if carte==['5 de ♣']:
        card = pygame.image.load("cartes/5♣.png").convert()
        valeur=5
    if carte==['6 de ♣']:
        card = pygame.image.load("cartes/6♣.png").convert()
        valeur=6
    if carte==['7 de ♣']:
        card = pygame.image.load("cartes/7♣.png").convert()
        valeur=7
    if carte==['8 de ♣']:
        card = pygame.image.load("cartes/8♣.png").convert()
        valeur=8
    if carte==['9 de ♣']:
        card = pygame.image.load("cartes/9♣.png").convert()
        valeur=9
    if carte==['10 de ♣']:
        card = pygame.image.load("cartes/10♣.png").convert()
        valeur=10
    if carte==['Valet de ♣']:
        card = pygame.image.load("cartes/J♣.png").convert()
        valeur=10
    if carte==['Dame de ♣']:
        card = pygame.image.load("cartes/Q♣.png").convert()
        valeur=10
    if carte==['Roi de ♣']:
        card = pygame.image.load("cartes/K♣.png").convert()
        valeur=10

    if carte==['as de ♥']:
        card = pygame.image.load("cartes/as♥.png").convert()
        valeur = 1
    if carte==['2 de ♥']:
        card = pygame.image.load("cartes/2♥.png").convert()
        valeur=2
    if carte==['3 de ♥']:
        card = pygame.image.load("cartes/3♥.png").convert()
        valeur=3
    if carte==['4 de ♥']:
        card = pygame.image.load("cartes/4♥.png").convert()
        valeur=4
    if carte==['5 de ♥']:
        card = pygame.image.load("cartes/5♥.png").convert()
        valeur=5
    if carte==['6 de ♥']:
        card = pygame.image.load("cartes/6♥.png").convert()
        valeur=6
    if carte==['7 de ♥']:
        card = pygame.image.load("cartes/7♥.png").convert()
        valeur=7
    if carte==['8 de ♥']:
        card = pygame.image.load("cartes/8♥.png").convert()
        valeur=8
    if carte==['9 de ♥']:
        card = pygame.image.load("cartes/9♥.png").convert()
        valeur=9
    if carte==['10 de ♥']:
        card = pygame.image.load("cartes/10♥.png").convert()
        valeur=10
    if carte==['Valet de ♥']:
        card = pygame.image.load("cartes/J♥.png").convert()
        valeur=10
    if carte==['Dame de ♥']:
        card = pygame.image.load("cartes/Q♥.png").convert()
        valeur=10
    if carte==['Roi de ♥']:
        card = pygame.image.load("cartes/K♥.png").convert()
        valeur=10

    if carte==['as de ♦']:
        card = pygame.image.load("cartes/as♦.png").convert()
        valeur = 1
    if carte==['2 de ♦']:
        card = pygame.image.load("cartes/2♦.png").convert()
        valeur=2
    if carte==['3 de ♦']:
        card = pygame.image.load("cartes/3♦.png").convert()
        valeur=3
    if carte==['4 de ♦']:
        card = pygame.image.load("cartes/4♦.png").convert()
        valeur=4
    if carte==['5 de ♦']:
        card = pygame.image.load("cartes/5♦.png").convert()
        valeur=5
    if carte==['6 de ♦']:
        card = pygame.image.load("cartes/6♦.png").convert()
        valeur=6
    if carte==['7 de ♦']:
        card = pygame.image.load("cartes/7♦.png").convert()
        valeur=7
    if carte==['8 de ♦']:
        card = pygame.image.load("cartes/8♦.png").convert()
        valeur=8
    if carte==['9 de ♦']:
        card = pygame.image.load("cartes/9♦.png").convert()
        valeur=9
    if carte==['10 de ♦']:
        card = pygame.image.load("cartes/10♦.png").convert()
        valeur=10
    if carte==['Valet de ♦']:
        card = pygame.image.load("cartes/J♦.png").convert()
        valeur=10
    if carte==['Dame de ♦']:
        card = pygame.image.load("cartes/Q♦.png").convert()
        valeur=10
    if carte==['Roi de ♦']:
        card = pygame.image.load("cartes/K♦.png").convert()
        valeur=10

    del carte
    return (card)                                                       #on retourne la valeur card qui est une image et "valeur" (si ca marche)

def tirage_de_la_carte2():
    from initpaquet import paquets
    import pygame


    pygame.init()
    valeur=int
    carte = paquets()[:1] #on tire une carte
    del paquets()[:1] #on l'enlève du paquet

    if carte==['as de ♠']:                                                       # si la carte est un 'as de ♠'
        card = pygame.image.load("cartes/as♠.png").convert()                     # alors on affiche la carte 2♠ du document cartes
        valeur=1
    if carte==['2 de ♠']:
        card = pygame.image.load("cartes/2♠.png").convert()                      # de même pour les autre cartes
        valeur=2
    if carte==['3 de ♠']:
        card = pygame.image.load("cartes/3♠.png").convert()
        valeur=2
    if carte==['4 de ♠']:
       card = pygame.image.load("cartes/4♠.png").convert()
       valeur=4
    if carte==['5 de ♠']:
        card = pygame.image.load("cartes/5♠.png").convert()
        valeur=5
    if carte==['6 de ♠']:
        card = pygame.image.load("cartes/6♠.png").convert()
        valeur=6
    if carte==['7 de ♠']:
        card = pygame.image.load("cartes/7♠.png").convert()
        valeur=7
    if carte==['8 de ♠']:
        card = pygame.image.load("cartes/8♠.png").convert()
        valeur=8
    if carte==['9 de ♠']:
        card = pygame.image.load("cartes/9♠.png").convert()
        valeur=9
    if carte==['10 de ♠']:
        card = pygame.image.load("cartes/10♠.png").convert()
        valeur=10
    if carte==['Valet de ♠']:
        card = pygame.image.load("cartes/J♠.png").convert()
        valeur=10
    if carte==['Dame de ♠']:
        card = pygame.image.load("cartes/Q♠.png").convert()
        valeur=10
    if carte==['Roi de ♠']:
        card = pygame.image.load("cartes/K♠.png").convert()
        valeur=10

    if carte==['as de ♣']:
        card = pygame.image.load("cartes/as♣.png").convert()
        valeur=1
    if carte==['2 de ♣']:
        card = pygame.image.load("cartes/2♣.png").convert()
        valeur=2
    if carte==['3 de ♣']:
        card = pygame.image.load("cartes/3♣.png").convert()
        valeur=3
    if carte==['4 de ♣']:
        card = pygame.image.load("cartes/4♣.png").convert()
        valeur=4
    if carte==['5 de ♣']:
        card = pygame.image.load("cartes/5♣.png").convert()
        valeur=5
    if carte==['6 de ♣']:
        card = pygame.image.load("cartes/6♣.png").convert()
        valeur=6
    if carte==['7 de ♣']:
        card = pygame.image.load("cartes/7♣.png").convert()
        valeur=7
    if carte==['8 de ♣']:
        card = pygame.image.load("cartes/8♣.png").convert()
        valeur=8
    if carte==['9 de ♣']:
        card = pygame.image.load("cartes/9♣.png").convert()
        valeur=9
    if carte==['10 de ♣']:
        card = pygame.image.load("cartes/10♣.png").convert()
        valeur=10
    if carte==['Valet de ♣']:
        card = pygame.image.load("cartes/J♣.png").convert()
        valeur=10
    if carte==['Dame de ♣']:
        card = pygame.image.load("cartes/Q♣.png").convert()
        valeur=10
    if carte==['Roi de ♣']:
        card = pygame.image.load("cartes/K♣.png").convert()
        valeur=10

    if carte==['as de ♥']:
        card = pygame.image.load("cartes/as♥.png").convert()
        valeur = 1
    if carte==['2 de ♥']:
        card = pygame.image.load("cartes/2♥.png").convert()
        valeur=2
    if carte==['3 de ♥']:
        card = pygame.image.load("cartes/3♥.png").convert()
        valeur=3
    if carte==['4 de ♥']:
        card = pygame.image.load("cartes/4♥.png").convert()
        valeur=4
    if carte==['5 de ♥']:
        card = pygame.image.load("cartes/5♥.png").convert()
        valeur=5
    if carte==['6 de ♥']:
        card = pygame.image.load("cartes/6♥.png").convert()
        valeur=6
    if carte==['7 de ♥']:
        card = pygame.image.load("cartes/7♥.png").convert()
        valeur=7
    if carte==['8 de ♥']:
        card = pygame.image.load("cartes/8♥.png").convert()
        valeur=8
    if carte==['9 de ♥']:
        card = pygame.image.load("cartes/9♥.png").convert()
        valeur=9
    if carte==['10 de ♥']:
        card = pygame.image.load("cartes/10♥.png").convert()
        valeur=10
    if carte==['Valet de ♥']:
        card = pygame.image.load("cartes/J♥.png").convert()
        valeur=10
    if carte==['Dame de ♥']:
        card = pygame.image.load("cartes/Q♥.png").convert()
        valeur=10
    if carte==['Roi de ♥']:
        card = pygame.image.load("cartes/K♥.png").convert()
        valeur=10

    if carte==['as de ♦']:
        card = pygame.image.load("cartes/as♦.png").convert()
        valeur = 1
    if carte==['2 de ♦']:
        card = pygame.image.load("cartes/2♦.png").convert()
        valeur=2
    if carte==['3 de ♦']:
        card = pygame.image.load("cartes/3♦.png").convert()
        valeur=3
    if carte==['4 de ♦']:
        card = pygame.image.load("cartes/4♦.png").convert()
        valeur=4
    if carte==['5 de ♦']:
        card = pygame.image.load("cartes/5♦.png").convert()
        valeur=5
    if carte==['6 de ♦']:
        card = pygame.image.load("cartes/6♦.png").convert()
        valeur=6
    if carte==['7 de ♦']:
        card = pygame.image.load("cartes/7♦.png").convert()
        valeur=7
    if carte==['8 de ♦']:
        card = pygame.image.load("cartes/8♦.png").convert()
        valeur=8
    if carte==['9 de ♦']:
        card = pygame.image.load("cartes/9♦.png").convert()
        valeur=9
    if carte==['10 de ♦']:
        card = pygame.image.load("cartes/10♦.png").convert()
        valeur=10
    if carte==['Valet de ♦']:
        card = pygame.image.load("cartes/J♦.png").convert()
        valeur=10
    if carte==['Dame de ♦']:
        card = pygame.image.load("cartes/Q♦.png").convert()
        valeur=10
    if carte==['Roi de ♦']:
        card = pygame.image.load("cartes/K♦.png").convert()
        valeur=10

    del carte
    return ( valeur)




