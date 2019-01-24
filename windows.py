import pygame						# On importe pygame
from pygame.locals import *

def windows(): #création  de la fonction windows
	pygame.init()

	fenetre = pygame.display.set_mode((1145,720)) # on créer une fenêtre pygame de 11145/720 pixels

	return fenetre # renvoie la variable fenetre
