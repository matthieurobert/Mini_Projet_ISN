import pygame
from pygame.locals import *

def ajouter_1():
    import pygame

    somme=0
    pygame.init()
    somme=somme+1
    pygame.display.set_mode()
    if somme == 1:
        plus1 = pygame.image.load("nombres/1.png").convert()
    if somme == 2:
        plus1 = pygame.image.load('nombres/2.png').convert()
    if somme == 3:
        plus1 = pygame.image.load('nombres/3.png').convert()
    if somme == 4:
        plus1 = pygame.image.load('nombres/4.png').convert()
    if somme == 5:
        plus1 = pygame.image.load('nombres/5.png').convert()
    if somme == 6:
        plus1 = pygame.image.load('nombres/6.png').convert()
    if somme == 7:
        plus1 = pygame.image.load('nombres/7.png').convert()
    if somme == 8:
        plus1 = pygame.image.load('nombres/8.png').convert()
    if somme == 9:
        plus1 = pygame.image.load('nombres/9.png').convert()


    return plus1

def enlever_1():
    import pygame


    pygame.init()
    somme=somme-1

    if somme == 1:
        moins = pygame.image.load('nombres/1.png').convert()
    if somme == 2:
        moins = pygame.image.load('nombres/2.png').convert()
    if somme == 3:
        moins = pygame.image.load('nombres/3.png').convert()
    if somme == 4:
        moins = pygame.image.load('nombres/4.png').convert()
    if somme == 5:
        moins = pygame.image.load('nombres/5.png').convert()
    if somme == 6:
        moins = pygame.image.load('nombres/6.png').convert()
    if somme == 7:
        moins = pygame.image.load('nombres/7.png').convert()
    if somme == 8:
        moins = pygame.image.load('nombres/8.png').convert()

    return moins1

