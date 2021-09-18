
#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import os, sys
import bs4
from bs4 import BeautifulSoup
import requests
import smtplib #protocole internet, permet d'envoyer les mails
import time

headers ={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.123 Safari/537.36'}

url='https://www.amazon.fr/LABISTS-Alimentation-Interrupteur-Ventilateur-Dissipateur/dp/B07WBWK17Y'


def test_prix():
	resp = requests.get(url, headers=headers)#requete sur l'url

	s = BeautifulSoup(resp.content, features = 'lxml')
	product_title = s.select('#productTitle')[0].get_text().strip()
	product_price = s.select('#priceblock_ourprice')[0].get_text().strip().replace(',','.')#[0] retire les crochets, choisi le premier element d'une liste qu'on peut convertir en texte
	#x=s.find(id="productTitle").get_text()

	print(product_title)
	print("Le prix est de : " + product_price)

	ajustement_prix = float(product_price[:-3])

	#print(ajustement_prix)

	if(ajustement_prix > 90):
		send_mail()
	else:
		print("Dommage poto ! ")

	#print(ajustement_prix)

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('constantin.chtanko@gmail.com', 'rggymjrdtxczgqmo')#google app passwords

	subject = 'Le prix a diminue! '
	body = 'Visitez la page : https://www.amazon.fr/LABISTS-Alimentation-Interrupteur-Ventilateur-Dissipateur/dp/B07WBWK17Y'

	msg = f"Subject : {subject}\n\n{body}"

	server.sendmail( 'constantin.chtanko@etu.formation-aftec.com',
		'constantin.chtanko@gmail.com',
		msg#.encode('utf-8')
		)
	print("Un mail a ete envoye !" )

	server.quit()

while(True):
	test_prix()
	time.sleep(60)



#print(x).encode('utf-8')