def paquets():
	import random

	nombre=['as','2','3','4','5','6','7','8','9','10','Valet','Dame','Roi']        # on creer une liste contenant tous les nombres
	couleur=[' de ♥',' de ♦',' de ♠',' de ♣']                                      # on creer une liste contenant toutes les couleurs
	paquet=[]
	for x in range(0,12,1):
	    for y in range(0,3,1):
	        paquet.append(nombre[x]+couleur[y])                                    # on ajoute le nombre et une couleur

	random.shuffle(paquet)                                                         #on mélange la liste
	return paquet                                                                  # on renvoie la liste paquet

