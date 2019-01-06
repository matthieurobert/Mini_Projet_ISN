import pygame
from pygame.locals import *
from tirage_carte import tirage_de_la_carte 
from windows import windows

def continuer():
	continuer = 1

	while continuer:
		for event in pygame.event.get():
			if event.type == QUIT:    
				continuer = 0
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1 and 650<= event.pos[0] <= 825 and 625 <= event.pos[1] <= 719:
					carte2 = tirage_de_la_carte()
					fenetre = windows()
					fenetre.blit(carte2, (585,435))

			pygame.display.flip()
	