from pygame.locals import *
import pygame

def bouton_tirer():

	pygame.init()

	tirer = pygame.image.load("tirer.png").convert_alpha()                             #on charge l'image "tirer.png"

	return tirer # renvoyer la variable tirer

bouton_tirer #lance la fonction bouton_tirer