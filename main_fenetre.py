import pygame
from pygame.locals import *

def main():
    from tirage_carte import tirage_de_la_carte
    from tirer import bouton_tirer
    from windows import windows


    pygame.init()

    fenetre = windows()

    continuer = 1



    table = pygame.image.load("blackjack_table.png").convert()
    fenetre.blit(table, (0,0))

    carte = tirage_de_la_carte()
    fenetre.blit(carte, (485,435))

    croupier = pygame.image.load("croupier.png").convert()
    fenetre.blit(croupier, (485, 0))

    boutonTirage = bouton_tirer()
    fenetre.blit(boutonTirage, (650,625))

    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
       	    if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and 650<= event.pos[0] <= 825 and 625 <= event.pos[1] <= 719:
                    carte2 = tirage_de_la_carte()

                    fenetre.blit(carte2, (505,435))

            pygame.display.flip()


        pygame.display.flip()


main()
