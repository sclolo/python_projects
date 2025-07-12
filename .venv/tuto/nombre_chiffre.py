def nombre_chiffres(nombre, chiffre): 
	# Commençons par éliminer le cas particulier du nombre 0 
	if nombre == 0: 
		# Si on cherche le chiffre "0" il y est une fois. Si c'est un autre chiffre, fatalement il n'est pas 0 donc il n'y est pas 
		return 1 if chiffre == 0 else 0 
  
	# Cas particulier terminé, traitement des cas généraux 
	# On va maintenant compter la présence du chiffre demandé 
	compteur = 0 
  
	# Tant que le nombre n'est pas terminé, on le traite 
	while nombre != 0: 
		# Si le reste de la division par 10 donne le chiffre attendu, c'est que le chiffre est présent 
		if nombre % 10 == chiffre: compteur += 1 
  
		# Maintenant on divise le nombre par 10 pour éliminer son dernier chiffre qui a été examiné 
		nombre //= 10
  
	# On a fini de compter 
	return compteur 

print(nombre_chiffres(589270222454,2))

#Sinon avec les chaines de caractères
nbr = "589270222454"
ch = "2"
print (nbr.count(ch))
