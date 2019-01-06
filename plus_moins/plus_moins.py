from pygame.locals import *
import pygame

def bouton_plus():

	pygame.init()

	plus_im = pygame.image.load("plus.png").convert_alpha()

	return plus_im

def bouton_moins():

	pygame.init()

	moins_im = pygame.image.load("moins.png").convert_alpha()

	return moins_im