import pygame
from pygame.locals import *

def main():
	from tirage_carte import tirage_de_la_carte 
	from tirer import bouton_tirer
	pygame.init()

	fenetre = pygame.display.set_mode((1145,720))
	table = pygame.image.load("blackjack_table.png").convert()
	fenetre.blit(table, (0,0))

	carte = tirage_de_la_carte()
	fenetre.blit(carte, (485,435))

	boutonTirage = bouton_tirer()
	fenetre.blit(boutonTirage, (650,625))

	pygame.display.flip()

	

