import pygame
from pygame.locals import *
from main_fenetre import main
from mise import ajouter_1
from mise import enlever_1

def event():
    continuer = 1
    somme=0

    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and 400<= event.pos[0] <= 484 and 625 <= event.pos[1] <= 710:

                    plus = ajouter_1
                    window = main()
                    window.blit(plus,(35,400))

                if event.button == 1 and 300<= event.pos[0] <= 384 and 657 <= event.pos[1] <= 680:

                    moins = enlever_1
                    window = main()
                    window.blit(moins,(35,400))

        pygame.display.flip()
