def paquets():
	import random

	nombre=['as','2','3','4','5','6','7','8','9','10','Valet','Dame','Roi']
	couleur=[' de ♥',' de ♦',' de ♠',' de ♣']
	paquet=[]
	for x in range(0,12,1):
	    for y in range(0,3,1):
	        paquet.append(nombre[x]+couleur[y])

	random.shuffle(paquet)
	return paquet

