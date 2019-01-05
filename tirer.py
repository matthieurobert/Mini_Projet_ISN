from pygame.locals import *
import pygame

def bouton_tirer():

	pygame.init()

	tirer = pygame.image.load("tirer.png").convert()

	return tirer
bouton_tirer