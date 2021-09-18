import bs4#toujours importer le bs4 avant
import requests #permet l'acces aux url
from bs4 import BeautifulSoup
import smtplib #protocole internet, permet d'envoyer les mails
import time

url='https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/'
#dictionnaire nous donnant des informations sur le moteur de recherche
#on peut trouver les infos mozilla en tapant my user agent sur la barre de recherches du browser
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.123 Safari/537.36'}


def check_price():


	#page = requests.get(url)#appel de la page

	page = requests.get(url, headers=headers)#appel de la page
	soup = BeautifulSoup(page.content, 'html.parser')#permet de retirer des informations choisies

	soup1=BeautifulSoup(soup.prettify(),"html.parser")#attention à bien utiliser le prettify, sinon il ne trouve rien par l'id

	#soup=bs4.BeautifulSoup(page.text, 'lxml')
	#print(soup)
	#print(soup.prettify())#voir le rendu détaillé
	print("===============================DEBUT============================================")
	print("\n\n")
	#soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span')
	

	title = soup1.find(id='productTitle').get_text()#get text enlevera les balises

	prix =soup1.find(id='priceblock_ourprice').get_text().replace(',','.')# on peut rajouter get_text pour convertir en string et remplacer la virgule en point pour le convertir en float
	converted_price = float(prix[1:-3])#nous souhaitons prendre le chiffre pour le coparer plus tard, on peut convertir en float

	if(converted_price>1.700): #attention aux points
		send_mail()
	else:
		print("Dommage poto !")

	print(converted_price)
	print(title.strip())#strip enleve les espaces en trop

	print("\n\n")
	print("================================FIN============================================")


def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)#google gmail, numero de connexion
	server.ehlo()#commande faite par un mail au serveur pour s'identifier lorsque celui ci se connecte à un autre serveur et commence le process d'envoi de mail
	server.starttls()#cryptage de connexion
	server.ehlo()
	server.login('constantin.chtanko@gmail.com', 'pkdnrkfjfxnlfsfd')

	subject = 'Le prix à diminué ! '
	body = 'Visitez la page Amazon https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_2?dchild=1&keywords=sony+a7&qid=1587728119&sr=8-3'

	msg = f"Subject : {subject}\n\n{body}"   #interpolation du sujet avec le "f"
	#smtp.sendmail(from_entry.get(),to_entry.get(),msg_entry.get())
	server.sendmail( 
		'constantin.chtanko@etu.formation-aftec.com',

		'constantin.chtanko@gmail.com',#le mail sera envoyé sur cette ligne 
		
		msg.encode('utf-8')#recodage en utf-8 car probleme de lecture en ascii
		)
	#envoi d'un email

	print('Un mail à été envoyé ! ')

	server.quit()#fermeture du serveur après envoi

while(True):

	check_price()
	time.sleep(3600)#verifie les prix toutes les heures