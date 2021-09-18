import requests
import bs4
from bs4 import BeautifulSoup
import csv

#creationd de listes receuillant les infos
dateList=[]
highList=[]
MarketCap=[]

url = 'https://coinmarketcap.com/currencies/bitcoin-sv/historical-data/?start=20130429&end=20200419'
r = requests.get(url)
soup=bs4.BeautifulSoup(r.text,'lxml')

#scriptCoin = soup.find('tr',  {'class' : 'cmc-table-row'}).find('td', {'class':
#	'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--left'}).text
tr = soup.find_all('tr', {'class':'cmc-table-row'})
for item in tr:
	dateList.append(item.find('td', {'class':'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--left'}).text)
	highList.append(item.find_all('td')[2].text)#3eme colonne du tableau de valeurs
	MarketCap.append(item.find_all('td')[6].text)#7eme colonne  du tableau de valeurs
#print(dateList)
#print(highList)
#print(MarketCap)

row0=['Date','Maximum', 'Capital du marche']#les en têtes pour le fichier csv qu'on va générer plus tard (titres)
rows=zip(dateList,highList,MarketCap)#les informations contenues dans les listes sont zippées

with open('coinMarketScraping_02_05_2020_gros_test.csv','w', encoding="utf-8", newline='') as csvfile:#w pour ecrire dans le fichier
	links_writer=csv.writer(csvfile)
	links_writer.writerow(row0)#écris le paragraphe
	for item in rows:#boucle remplissant le fichier avec les informations scrappees
		links_writer.writerow(item)#ecriture par chaque colonne
		
