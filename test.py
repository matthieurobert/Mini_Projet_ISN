import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1280,720), FULLSCREEN)
table = pygame.image.load("blackjack_table.png").convert()
fenetre.blit(table, (0,0))

perso = pygame.image.load("card_b_h9.png").convert()
fenetre.blit(perso, (485,435))

pygame.display.flip()

continuer = 1

while continuer:
	continuer = int(input())
