def cartes(carte, x, y):
	import pygame
	from pygame.locals import *

	pygame.init()

	# p = pic
	# t = trèfle
	# co = coeur 
	# ca = carreau 

	as_p = pygame.image.load("cartes/as♠.png").convert()
	2_p = pygame.image.load("cartes/2♠.png").convert()
	3_p = pygame.image.load("cartes/3♠.png").convert()
	4_p = pygame.image.load("cartes/4♠.png").convert()
	5_p = pygame.image.load("cartes/5♠.png").convert()
	6_p = pygame.image.load("cartes/6♠.png").convert()
	7_p = pygame.image.load("cartes/7♠.png").convert()
	8_p = pygame.image.load("cartes/8♠.png").convert()
	9_p = pygame.image.load("cartes/9♠.png").convert()
	10_p = pygame.image.load("cartes/10♠.png").convert()
	J_p = pygame.image.load("cartes/J♠.png").convert()
	Q_p = pygame.image.load("cartes/Q♠.png").convert()
	K_p = pygame.image.load("cartes/K♠.png").convert()

	as_t = pygame.image.load("cartes/as♣.png").convert()
	2_t = pygame.image.load("cartes/2♣.png").convert()
	3_t = pygame.image.load("cartes/3♣.png").convert()
	4_t = pygame.image.load("cartes/4♣.png").convert()
	5_t = pygame.image.load("cartes/5♣.png").convert()
	6_t = pygame.image.load("cartes/6♣.png").convert()
	7_t = pygame.image.load("cartes/7♣.png").convert()
	8_t = pygame.image.load("cartes/8♣.png").convert()
	9_t = pygame.image.load("cartes/9♣.png").convert()
	10_t = pygame.image.load("cartes/10♣.png").convert()
	J_t = pygame.image.load("cartes/J♣.png").convert()
	Q_t = pygame.image.load("cartes/Q♣.png").convert()
	K_t = pygame.image.load("cartes/K♣.png").convert()

	as_co = pygame.image.load("cartes/as♥.png").convert()
	2_co = pygame.image.load("cartes/2♥.png").convert()
	3_co = pygame.image.load("cartes/3♥.png").convert()
	4_co = pygame.image.load("cartes/4♥.png").convert()
	5_co = pygame.image.load("cartes/5♥.png").convert()
	6_co = pygame.image.load("cartes/6♥.png").convert()
	7_co = pygame.image.load("cartes/7♥.png").convert()
	8_co = pygame.image.load("cartes/8♥.png").convert()
	9_co = pygame.image.load("cartes/9♥.png").convert()
	10_co = pygame.image.load("cartes/10♥.png").convert()
	J_co = pygame.image.load("cartes/J♥.png").convert()
	Q_co = pygame.image.load("cartes/Q♥.png").convert()
	K_co = pygame.image.load("cartes/K♥.png").convert()

	as_ca = pygame.image.load("cartes/as♦.png").convert()
	2_ca = pygame.image.load("cartes/2♦.png").convert()
	3_ca = pygame.image.load("cartes/3♦.png").convert()
	4_ca = pygame.image.load("cartes/4♦.png").convert()
	5_ca = pygame.image.load("cartes/5♦.png").convert()
	6_ca = pygame.image.load("cartes/6♦.png").convert()
	7_ca = pygame.image.load("cartes/7♦.png").convert()
	8_ca = pygame.image.load("cartes/8♦.png").convert()
	9_ca = pygame.image.load("cartes/9♦.png").convert()
	10_ca = pygame.image.load("cartes/10♦.png").convert()
	J_ca = pygame.image.load("cartes/J♦.png").convert()
	Q_ca = pygame.image.load("cartes/Q♦.png").convert()
	K_ca = pygame.image.load("cartes/K♦.png").convert()

	fenetre.blit(im-carte, (x,y))
