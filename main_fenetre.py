import pygame
from pygame.locals import *

def main():
    from tirage_carte import tirage_de_la_carte
    from tirage_carte import tirage_de_la_carte2                                    # on importe tous les programmes dont nous avons besoins
    from perdu_gagné  import PERDU
    from perdu_gagné  import GAGNE
    from tirer import bouton_tirer
    from windows import windows
    from stop import bouton_stop



    somme=0                                                                     # la valeur des cartes

    fenetre = windows()                                                          # on créer une fenêtre

    continuer = 1

    pygame.init()                                                                # on rafraichi la fenêtre

    table = pygame.image.load("blackjack_table.png").convert()                   # on importe l'image "blackjack_table.png"
    fenetre.blit(table, (0,0))                                                   #on l'affiche à partir des coordonnées 0,0

    carte = tirage_de_la_carte()                                                 # on récupère la carte du programme tirage_de_la_carte
    fenetre.blit(carte, (485,435))                                               # dont la résultante et l'image obtenue Ex: 1♣.png
    somme = somme + tirage_de_la_carte2()
    print(somme)



    carte = tirage_de_la_carte()                                                 # on refait de même mais avec une autre carte
    fenetre.blit(carte, (505,435))                                               # on la décalle de 20 pixels par rapport à l'autre carte
    somme = somme + tirage_de_la_carte2()
    print(somme)

    boutonTirage = bouton_tirer()                                                #on affiche le bouton tirer
    fenetre.blit(boutonTirage, (650,625))                                       #on l'affiche aux coordonnées 650,625

    boutonSTOP = bouton_stop()
    fenetre.blit(boutonSTOP,(400,625))

    while continuer:                                                             # boucle qui permet de garder la fenêtre ouverte
        for event in pygame.event.get():                                         # si il y a un événement de type "CLICK" faire:
            if event.type == QUIT:                                               # si l'événement est de type quitter alors on ferme la fenêtre
                continuer = 0
       	    if event.type == MOUSEBUTTONDOWN:                                    # si l'on clique avec la souris:
                if event.button == 1 and 650<= event.pos[0] <= 825 and 625 <= event.pos[1] <= 719: # si le clic est dans cette zone ( TIRER ) :
                    carte2 = tirage_de_la_carte()                                # importe une carte
                    somme = somme + tirage_de_la_carte2()
                    print(somme)
                    fenetre.blit(carte2, (525,435))                             # affiche la carte
                    pygame.display.flip()

                if event.button == 1 and 400<= event.pos[0] <= 575 and 625 <= event.pos[1] <= 719:

                    #CROUPIER A FAIRE#
                    print("c pas fini ...")

            if somme > 21:
                perdu = PERDU()
                fenetre.blit(perdu,(250,215))
                continuer = 0









            pygame.display.flip()                                                # raffraichi la fenêtre


        pygame.display.flip()                                                    # raffraichi la fenêtre



