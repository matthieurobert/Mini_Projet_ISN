import pygame
from pygame.locals import *
import carte

pygame.init()

fenetre = pygame.display.set_mode((1280,720), FULLSCREEN)
table = pygame.image.load("blackjack_table.png").convert()
fenetre.blit(table, (0,0))

cartes(as_p, 485, 435)

pygame.display.flip()

continuer = 1

while continuer:
	continuer = int(input())
