import pygame						# On importe pygame
from pygame.locals import *

def windows():						# On créer la fonction windows
	pygame.init()					# On initialise pygame

	fenetre = pygame.display.set_mode((1145,720))    # On créer la fenêtre et on la stocke dans une variable
	
	return fenetre                  # On renvoie la variable fenetre
