import bs4
import requests
from bs4 import BeautifulSoup

def parsePrix():
	url='https://finance.yahoo.com/quote/FB'
	r= requests.get(url)
	soup=bs4.BeautifulSoup(r.text, 'lxml')

	#scriptYahoo = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})#trouver et copier la div exacte en précisant la classe
	#scriptYahoo = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span')#on peut aussi ajouter [0] pour préciser qu'on va chercher les infos dans la premiere balise
	scriptYahoo = soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text#enlever et find_all et rajouter la balise recherchée dans la balise

	#print(scriptYahoo)

	return scriptYahoo

while True: #boucle retournant le prix à chaque mise à jour
	print("Le prix actuel est : " + str(parsePrix()))
