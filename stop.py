from pygame.locals import *
import pygame

def bouton_stop():

	pygame.init()

	tirer = pygame.image.load("stop.png").convert_alpha()                             #on charge l'image "stop.png"
	#image.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
	return tirer

