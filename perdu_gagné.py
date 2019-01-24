from pygame.locals import *   # On importe pygame
import pygame

def PERDU():  # Création de la fonction perdu

    pygame.init() # initialisation de pygame

    perdu = pygame.image.load("perdu.png").convert_alpha()  # On charge l'image perdu.png et on la stocke dans la variable perdu

    return PERDU # On renvoie la variable perdu



def GAGNE():  # Création de la fonction gagné

    pygame.init()  # On initialise pygame

    gagne = pygame.image.load("gagné.png").convert_alpha() # On charge l'image gagné.png et on la stoke dans la variable gagne

    return(gagne)  # On renvoie la variable gagne