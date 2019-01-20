from pygame.locals import *
import pygame

def bouton_tirer():

	pygame.init()

	tirer = pygame.image.load("tirer.png").convert_alpha()                             #on charge l'image "tirer.png"
	#image.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
	return tirer

bouton_tirer