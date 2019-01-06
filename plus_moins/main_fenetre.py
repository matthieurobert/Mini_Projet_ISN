import pygame
from pygame.locals import *

def main():
    from plus_moins import bouton_plus
    from plus_moins import bouton_moins

    pygame.init()

    fenetre = pygame.display.set_mode((1145,720))
    table = pygame.image.load("blackjack_table.png").convert()

    fenetre.blit(table, (0,0))

    boutonPlus = bouton_plus()
    fenetre.blit(boutonPlus, (400,625))

    boutonMoins = bouton_moins()
    fenetre.blit(boutonMoins, (300,657))

    pygame.display.flip()

    return fenetre

