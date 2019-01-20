import pygame
from pygame.locals import *

def main():
    from tirage_carte import tirage_de_la_carte                                    # on importe tous les programmes dont nous avons besoins
    from perdu_gagné  import PERDU
    from perdu_gagné  import GAGNE
    from tirer import bouton_tirer
    from windows import windows
    from stop import bouton_stop



    somme=0                                                                     # la valeur des cartes
    croupier= 0

    fenetre = windows()                                                          # on créer une fenêtre

    continuer = 1

    pygame.init()                                                                # on initialise pygame

    table = pygame.image.load("blackjack_table.png").convert()                   # on importe l'image "blackjack_table.png"
    fenetre.blit(table, (0,0))                                                   #on l'affiche à partir des coordonnées 0,0

    carte = tirage_de_la_carte()                                                 # on récupère la carte du programme tirage_de_la_carte
    fenetre.blit(carte[0], (485,435))                                               # dont la résultante et l'image obtenue Ex: 1♣.png
    somme = somme + carte[1]
    print(somme)

    pos_player = 525
    pos_croup = 485


    carte = tirage_de_la_carte()                                                 # on refait de même mais avec une autre carte
    fenetre.blit(carte[0], (505,435))                                               # on la décalle de 20 pixels par rapport à l'autre carte
    somme = somme + carte[1]
    print(somme)

    boutonTirage = bouton_tirer()                                                #on affiche le bouton tirer
    fenetre.blit(boutonTirage, (875,625))                                       #on l'affiche aux coordonnées 650,625

    boutonSTOP = bouton_stop()
    fenetre.blit(boutonSTOP,(90,625))

    while continuer:                                                             # boucle qui permet de garder la fenêtre ouverte
        for event in pygame.event.get():                                         # si il y a un événement de type "CLICK" faire:
            if event.type == QUIT:                                               # si l'événement est de type quitter alors on ferme la fenêtre
                continuer = 0
       	    if event.type == MOUSEBUTTONDOWN:                                    # si l'on clique avec la souris:
                if event.button == 1 and 875<= event.pos[0] <= 1050 and 625 <= event.pos[1] <= 719: # si le clic est dans cette zone ( TIRER ) :
                    carte2 = tirage_de_la_carte()                                # importe une carte
                    somme = somme + carte2[1]
                    
                    print(somme)
                    fenetre.blit(carte2[0], (pos_player,435))                             # affiche la carte
                    pos_player = pos_player + 20
                    pygame.display.flip()

                    if somme > 21 :
                    	perdu = PERDU()
                    	fenetre.blit(perdu,(250,215))
                    	continuer = 0

                if event.button == 1 and 90<= event.pos[0] <= 575 and 625 <= event.pos[1] <= 719:
                	if croupier == 0 :
                		carte_croup1 =tirage_de_la_carte()
                		croupier = croupier + carte_croup1[1]
                		print("c o croupier")
                		print(croupier)

                		fenetre.blit(carte_croup1[0], (pos_croup, 50))
                		pos_croup = pos_croup + 20
                		pygame.display.flip()

                		carte_croup2 = tirage_de_la_carte()
                		croupier = croupier + carte_croup2[1]

                		print(croupier)
                		fenetre.blit(carte_croup2 [0], (pos_croup, 50))
                		pos_croup = pos_croup + 20
                		pygame.display.flip()

                		while croupier <= 17:
                			carte_croup3 = tirage_de_la_carte()
                			croupier = croupier + carte_croup3[1]

                			print(croupier)

                			fenetre.blit(carte_croup3[0], (pos_croup, 50))
                			pos_croup = pos_croup + 20
                			pygame.display.flip()

        if croupier >= 1:

        	if (somme > 21 and somme < croupier) or croupier == 21:
        		perdu = PERDU()
        		fenetre.blit(perdu,(250,215))
        		continuer = 0

        	elif somme > croupier or croupier > 21:
        		gagne = GAGNE()
        		fenetre.blit(gagne,(250,215))
        		continuer = 0

        	pygame.display.flip()                                                # raffraichi la fenêtre
        pygame.display.flip()                                                    # raffraichi la fenêtre



