import requests
from bs4 import BeautifulSoup
import time

#preciser un url dans lequel on va stocker une page web
#ne pas oublier de preciser le protocole et les slashs

#url = 'http://example.webscraping.com'

"""
links = [] #création d'une liste pour strocker le contenu des td

for i in range(26):#parcours de 26 indices qui representeront les pages du site
	url = 'http://example.webscraping.com/places/default/index/' + str(i) #parcours de l'url avec la concatenation du dernier index	
	response = requests.get(url)#requete get
	print(response)


	if response.ok: #si on a un code '200', sinon la condition ne s'execute pas, si la réponse est bonne
		print('Page : ' + str(i))

		soup = BeautifulSoup(response.text, 'lxml')#le resultat du contenu de l'html de la réponse, preciser lxml 
		#print(soup)#text permet d'avoir le contenu de la reponse et donc le script de la page html, 
		#permet de parser et chercher les elements à l'intérieur
		#title = soup.find('title')#fonctions permettant de localiser un element en fonction d'un localiseur css
		tds = soup.findAll('td')#selectionne plusieurs elements
		#preciser le nom de la balise
		#print(title.text)#avoir le contenu sans les balises avec .text
		#print(len(tds))#afficher la longueur de la variable tds, le nombre de td dans la page
		#prends tout le contenu des td et affiche 
		#[print(str(td) + '\n\n') for td in tds] 
		#ajout de la boucle parcourant tous les td avec la concatenation \n pour le retour à la ligne
		
		for td in tds:#une autre façon d'écrire la boucle, pour chaque element td dans tds
			a=td.find('a')#trouver une balise a à l'intérieur du td pour avoir le contenu
			link = a['href']#on veut extraire un attribut à l'intérieur du balise, on utilise des crochets, pour chaque a on cherche l'attribut href
			links.append('http://example.webscraping.com'+link)#ajout dans la liste, on concatene avec l'adresse du site pour reconstituer les liens
			time.sleep(1)#la boucle fait une pause de 1 à chauque parcours

print(len(links))#affiche le nombre de resultats contenus dans la liste

with open('urls.txt', 'w') as file: #fonction open permet d'ouvrir un fichier, w : argument pour passer en mode ecriture
	for link in links:#boucle parcourant la liste des liens
		file.write(link + '\n')#ecriture dans le fichier des liens
"""
with open('urls.txt', 'r') as file: # r : ouverture en lecture
	with open('pays.csv', 'w') as outf: #boucle creant un fichier csv dans lequel on va écrire
		outf.write('Pays,Population\n') #ecriture des en tetes
		for row in file:		
			#repetition du scrapping mais dans une seule page
			url = row.strip()#a la place de l'url http://example.webscraping.com/places/default/view/Yemen-250' , pour retirer les retours à la ligne

			response = requests.get(url)
			if response.ok:
				soup = BeautifulSoup(response.text, 'lxml')
				#capture des selecteurs css dont on a besoin
				#trouver la balise tr, class comme clé et contenu la balise contenant le pays	
				#puis rechercher à l'intérieur du tr la balise td avec pour clé la classe w2p_fw
				country = soup.find('tr', {'id': 'places_country__row'}).find('td', {'class':'w2p_fw'})
				pop = soup.find('tr', {'id':'places_population__row'}).find('td', {'class':'w2p_fw'})
				print('Pays : ' + country.text + ', Population : ' + pop.text)
				outf.write(country.text + ',' + pop.text.replace(',','') + '\n')#les virgules sont remplacés par rien afin de ne pas faire une nouvelle colonne
			time.sleep(1)

