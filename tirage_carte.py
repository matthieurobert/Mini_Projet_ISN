from pygame.locals import *
def tirage_de_la_carte():
    from initpaquet import paquets
    import pygame


    pygame.init()

    carte = paquets()[:1] #on tire une carte
    del paquets()[:1] #on l'enlève du paquet

    if carte==['as de ♠']:
        card = pygame.image.load("cartes/as♠.png").convert()
    if carte==['2 de ♠']:
        card = pygame.image.load("cartes/2♠.png").convert()
    if carte==['3 de ♠']:
        card = pygame.image.load("cartes/3♠.png").convert()
    if carte==['4 de ♠']:
       card = pygame.image.load("cartes/4♠.png").convert()
    if carte==['5 de ♠']:
        card = pygame.image.load("cartes/5♠.png").convert()
    if carte==['6 de ♠']:
        card = pygame.image.load("cartes/6♠.png").convert()
    if carte==['7 de ♠']:
        card = pygame.image.load("cartes/7♠.png").convert()
    if carte==['8 de ♠']:
        card = pygame.image.load("cartes/8♠.png").convert()
    if carte==['9 de ♠']:
        card = pygame.image.load("cartes/9♠.png").convert()
    if carte==['10 de ♠']:
        card = pygame.image.load("cartes/10♠.png").convert()
    if carte==['Valet de ♠']:
        card = pygame.image.load("cartes/J♠.png").convert()
    if carte==['Dame de ♠']:
        card = pygame.image.load("cartes/Q♠.png").convert()
    if carte==['Roi de ♠']:
        card = pygame.image.load("cartes/K♠.png").convert()

    if carte==['as de ♣']:
        card = pygame.image.load("cartes/as♣.png").convert()
    if carte==['2 de ♣']:
        card = pygame.image.load("cartes/2♣.png").convert()
    if carte==['3 de ♣']:
        card = pygame.image.load("cartes/3♣.png").convert()
    if carte==['4 de ♣']:
        card = pygame.image.load("cartes/4♣.png").convert()
    if carte==['5 de ♣']:
        card = pygame.image.load("cartes/5♣.png").convert()
    if carte==['6 de ♣']:
        card = pygame.image.load("cartes/6♣.png").convert()
    if carte==['7 de ♣']:
        card = pygame.image.load("cartes/7♣.png").convert()
    if carte==['8 de ♣']:
        card = pygame.image.load("cartes/8♣.png").convert()
    if carte==['9 de ♣']:
        card = pygame.image.load("cartes/9♣.png").convert()
    if carte==['10 de ♣']:
        card = pygame.image.load("cartes/10♣.png").convert()
    if carte==['Valet de ♣']:
        card = pygame.image.load("cartes/J♣.png").convert()
    if carte==['Dame de ♣']:
        card = pygame.image.load("cartes/Q♣.png").convert()
    if carte==['Roi de ♣']:
        card = pygame.image.load("cartes/K♣.png").convert()

    if carte==['as de ♥']:
        card = pygame.image.load("cartes/as♥.png").convert()
    if carte==['2 de ♥']:
        card = pygame.image.load("cartes/2♥.png").convert()
    if carte==['3 de ♥']:
        card = pygame.image.load("cartes/3♥.png").convert()
    if carte==['4 de ♥']:
        card = pygame.image.load("cartes/4♥.png").convert()
    if carte==['5 de ♥']:
        card = pygame.image.load("cartes/5♥.png").convert()
    if carte==['6 de ♥']:
        card = pygame.image.load("cartes/6♥.png").convert()
    if carte==['7 de ♥']:
        card = pygame.image.load("cartes/7♥.png").convert()
    if carte==['8 de ♥']:
        card = pygame.image.load("cartes/8♥.png").convert()
    if carte==['9 de ♥']:
        card = pygame.image.load("cartes/9♥.png").convert()
    if carte==['10 de ♥']:
        card = pygame.image.load("cartes/10♥.png").convert()
    if carte==['Valet de ♥']:
        card = pygame.image.load("cartes/J♥.png").convert()
    if carte==['Dame de ♥']:
        card = pygame.image.load("cartes/Q♥.png").convert()
    if carte==['Roi de ♥']:
        card = pygame.image.load("cartes/K♥.png").convert()

    if carte==['as de ♦']:
        card = pygame.image.load("cartes/as♦.png").convert()
    if carte==['2 de ♦']:
        card = pygame.image.load("cartes/2♦.png").convert()
    if carte==['3 de ♦']:
        card = pygame.image.load("cartes/3♦.png").convert()
    if carte==['4 de ♦']:
        card = pygame.image.load("cartes/4♦.png").convert()
    if carte==['5 de ♦']:
        card = pygame.image.load("cartes/5♦.png").convert()
    if carte==['6 de ♦']:
        card = pygame.image.load("cartes/6♦.png").convert()
    if carte==['7 de ♦']:
        card = pygame.image.load("cartes/7♦.png").convert()
    if carte==['8 de ♦']:
        card = pygame.image.load("cartes/8♦.png").convert()
    if carte==['9 de ♦']:
        card = pygame.image.load("cartes/9♦.png").convert()
    if carte==['10 de ♦']:
        card = pygame.image.load("cartes/10♦.png").convert()
    if carte==['Valet de ♦']:
        card = pygame.image.load("cartes/J♦.png").convert()
    if carte==['Dame de ♦']:
        card = pygame.image.load("cartes/Q♦.png").convert()
    if carte==['Roi de ♦']:
        card = pygame.image.load("cartes/K♦.png").convert()

    del carte
    return card






