tableau = []
def verification(valeur_entree):
	while valeur_entree.isdecimal() == False:
		valeur_entree = input("Entrer un nombre correct : ")
	tableau.append(valeur_entree)
	

def comparerValeur(tab):
	if tab[0] > tab[1]:
		print(str(tab[0]) + " est sup à " + str(tab[1]))
	if tab[0] < tab[1]:
		print(str(tab[0]) + " est inférieur à " + str(tab[1]))
	if tab[0] == tab[1]:
		print(str(tab[0]) + " est égal à " + str(tab[1]))
		
		
nombre_1 = input("Entrer le premier nombre : ")
verification(nombre_1)
nombre_2 = input("Entrer le deuxième nombre : ")
verification(nombre_2)
comparerValeur(tableau)
