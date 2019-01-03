import pygame
from pygame.locals import *

def fermeture():
	continuer = 1

	while continuer:
		for event in pygame.event.get():   
			if event.type == QUIT:    
				continuer = 0

