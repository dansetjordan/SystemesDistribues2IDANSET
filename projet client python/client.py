# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:23:36 2020

@author: danset
"""

import requests


def AfficherUnProduit(code):
	path=("http://localhost:8989/produit/")
	
	r = requests.get(path + str(code))
	
	print(r.text)
	
def AjouterUnProduit(code,nom,prix):
	path=("http://localhost:8989/save/")
	
	r = requests.get( path + str(code) + "/" + str(nom) + "/" + str(prix))
	
	print(r.text)
	


#donnees=json.dumps(r.json)
#print(donnees)

while True:
	rep_infos = int(input("\n\nQuelles actions souhaitez-vous faire ?\n\n"
					   "1 - Afficher tous les produits ?\n"
					   "2 - Afficher un produit en fonction du code ?\n"
					   "3 - Sauvegarder un produit ?\n\n"
					   "Veuillez indiquer le chiffre correspondant : "))
	
	if rep_infos == 1:
		r = requests.get('http://localhost:8989/tous')
		print(r.text)
		
	elif rep_infos == 2:
		
		rep_code = int(input("Veuillez saisir l'id du produit ?\n\n"))
		
		if rep_code > 0:
			
			AfficherUnProduit(rep_code)
		else:
			
			print("erreur : l'id doit être supérieur à 0")
			break
	
	elif rep_infos == 3:
		
		rep_code = int(input("Veuillez saisir l'id du produit à ajouter ?\n\n"))
		
		if rep_code > 0:
			
			code = rep_code
		else:
			print("erreur : l'id doit être supérieur à 0")
			break
		
		rep_nom = input("Veuillez saisir le nom du produit à ajouter ?\n\n")
		
		if rep_nom != None:
			
			nom = rep_nom
		else:
			print("erreur : le nom est vide")
			break
		
		rep_prix = int(input("Veuillez saisir le prix du produit à ajouter ?\n\n"))
		
		if rep_prix > 0:
			
			prix = rep_prix
			AjouterUnProduit(code,nom,prix)
			
		else:
			print("erreur : le prix doit être supérieur à 0")
			break
		
	
	else:
		break
	


	