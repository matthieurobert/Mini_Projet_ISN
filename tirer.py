from pygame.locals import *
import pygame

def bouton_tirer():

	pygame.init()

	tirer = pygame.image.load("tirer.png").convert()                             #on charge l'image "tirer.png"

	return tirer

bouton_tirer