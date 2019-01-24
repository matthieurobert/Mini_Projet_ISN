from pygame.locals import *
import pygame

def bouton_stop():

	pygame.init()

	tirer = pygame.image.load("stop.png").convert_alpha()                             #on charge l'image "stop.png"
	
	return tirer

