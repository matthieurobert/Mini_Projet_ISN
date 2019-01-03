import pygame
from pygame.locals import *
from tirage_carte import tirage_de_la_carte 
from main_fenetre import main

def event():
	continuer = 1

	while continuer:
		for event in pygame.event.get():   
			if event.type == QUIT:    
				continuer = 0

			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1 and 650<= event.pos[0] <= 825 and 625 <= event.pos[1] <= 719:
					carte = tirage_de_la_carte()
					window = main()
					window.blit(carte, (585,435))

		pygame.display.flip()

