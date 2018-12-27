from pygame.locals import *
def tirage_de_la_carte():
    from initpaquet import paquet
    import pygame


    pygame.init()

    carte=paquet[:1] #on tire une carte
    del paquet[:1] #on l'enlève du paquet

    if carte==['as de ♠']:
        carte = pygame.image.load("as♠.png").convert()
    if carte==['2 de ♠']:
        carte = pygame.image.load("2♠.png").convert()
    if carte==['3 de ♠']:
        carte = pygame.image.load("3♠.png").convert()
    if carte==['4 de ♠']:
        carte = pygame.image.load("4♠.png").convert()
    if carte==['5 de ♠']:
        carte = pygame.image.load("5♠.png").convert()
    if carte==['6 de ♠']:
        carte = pygame.image.load("6♠.png").convert()
    if carte==['7 de ♠']:
        carte = pygame.image.load("7♠.png").convert()
    if carte==['8 de ♠']:
        carte = pygame.image.load("8♠.png").convert()
    if carte==['9 de ♠']:
        carte = pygame.image.load("9♠.png").convert()
    if carte==['10 de ♠']:
        carte = pygame.image.load("10♠.png").convert()
    if carte==['Valet de ♠']:
        carte = pygame.image.load("J♠.png").convert()
    if carte==['Dame de ♠']:
        carte = pygame.image.load("D♠.png").convert()
    if carte==['Roi de ♠']:
        carte = pygame.image.load("R♠.png").convert()

    if carte==['as de ♣']:
        carte = pygame.image.load("as♣.png").convert()
    if carte==['2 de ♣']:
        carte = pygame.image.load("2♣.png").convert()
    if carte==['3 de ♣']:
        carte = pygame.image.load("3♣.png").convert()
    if carte==['4 de ♣']:
        carte = pygame.image.load("4♣.png").convert()
    if carte==['5 de ♣']:
        carte = pygame.image.load("5♣.png").convert()
    if carte==['6 de ♣']:
        carte = pygame.image.load("6♣.png").convert()
    if carte==['7 de ♣']:
        carte = pygame.image.load("7♣.png").convert()
    if carte==['8 de ♣']:
        carte = pygame.image.load("8♣.png").convert()
    if carte==['9 de ♣']:
        carte = pygame.image.load("9♣.png").convert()
    if carte==['10 de ♣']:
        carte = pygame.image.load("10♣.png").convert()
    if carte==['Valet de ♣']:
        carte = pygame.image.load("V♣.png").convert()
    if carte==['Dame de ♣']:
        carte = pygame.image.load("D♣.png").convert()
    if carte==['Roi de ♣']:
        carte = pygame.image.load("R♣.png").convert()

    if carte==['as de ♥']:
        carte = pygame.image.load("as♥.png").convert()
    if carte==['2 de ♥']:
        carte = pygame.image.load("2♥.png").convert()
    if carte==['3 de ♥']:
        carte = pygame.image.load("3♥.png").convert()
    if carte==['4 de ♥']:
        carte = pygame.image.load("4♥.png").convert()
    if carte==['5 de ♥']:
        carte = pygame.image.load("5♥.png").convert()
    if carte==['6 de ♥']:
        carte = pygame.image.load("6♥.png").convert()
    if carte==['7 de ♥']:
        carte = pygame.image.load("7♥.png").convert()
    if carte==['8 de ♥']:
        carte = pygame.image.load("8♥.png").convert()
    if carte==['9 de ♥']:
        carte = pygame.image.load("9♥.png").convert()
    if carte==['10 de ♥']:
        carte = pygame.image.load("10♥.png").convert()
    if carte==['Valet de ♥']:
        carte = pygame.image.load("J♥.png").convert()
    if carte==['Dame de ♥']:
        carte = pygame.image.load("D♥.png").convert()
    if carte==['Roi de ♥']:
        carte = pygame.image.load("R♥.png").convert()

    if carte==['as de ♦']:
        carte = pygame.image.load("as♦.png").convert()
    if carte==['2 de ♦']:
        carte = pygame.image.load("2♦.png").convert()
    if carte==['3 de ♦']:
        carte = pygame.image.load("3♦.png").convert()
    if carte==['4 de ♦']:
        carte = pygame.image.load("4♦.png").convert()
    if carte==['5 de ♦']:
        carte = pygame.image.load("5♦.png").convert()
    if carte==['6 de ♦']:
        carte = pygame.image.load("6♦.png").convert()
    if carte==['7 de ♦']:
        carte = pygame.image.load("7♦.png").convert()
    if carte==['8 de ♦']:
        carte = pygame.image.load("8♦.png").convert()
    if carte==['9 de ♦']:
        carte = pygame.image.load("9♦.png").convert()
    if carte==['10 de ♦']:
        carte = pygame.image.load("10♦.png").convert()
    if carte==['Valet de ♦']:
        carte = pygame.image.load("J♦.png").convert()
    if carte==['Dame de ♦']:
        carte = pygame.image.load("D♦.png").convert()
    if carte==['Roi de ♦']:
        carte = pygame.image.load("R♦.png").convert()

    del carte

tirage_de_la_carte()





