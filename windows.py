import pygame
from pygame.locals import *

def windows():
	pygame.init()

	fenetre = pygame.display.set_mode((1145,720))
	
	return fenetre
