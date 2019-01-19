from pygame.locals import *
import pygame

def PERDU():

    pygame.init()

    perdu = pygame.image.load("perdu.png").convert_alpha()

    return perdu



def GAGNE():

    pygame.init()

    gagne = pygame.image.load("gagné.png").convert_alpha()