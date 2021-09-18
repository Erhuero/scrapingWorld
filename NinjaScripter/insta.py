import requests
from bs4 import BeautifulSoup
import re

#partie permettant de recuperer le contenu html de la page web
url = 'https://www.instagram.com/wearelikewise/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

script = soup.findAll('script', {'type' : 'text/javascript'}).text
#script = soup.find('div' , {'id' : 'react-root'}).find('span')
#test = soup.find('title').text
#[print(script) for script in scripts]#affiche tous les scripts grâce à la boucle for
#print(script[0])#premier script
#print(script[3])#quatrieme script a plus d'informations : le script JSON est comme un dictionnaire

#raw_data=script.replace(';', '')

print(script)