from pygame.locals import *
import pygame

def bouton_stop(): # création de la fonction bouton_stop

	pygame.init()

	tirer = pygame.image.load("stop.png").convert_alpha()                             #on charge l'image "stop.png"

	return tirer #on renvoie la variable tirer

