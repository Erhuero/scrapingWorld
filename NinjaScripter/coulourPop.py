import requests
import json
"""
Réseaux et paramètres
"""

#url de la requete json qu'on peut trouver dans firefox, examiner l'element, reseau, recherche GET + json, selection graphQL et recopier l'adresse
#de la page avec les "node" qui contiennent le lien qui nous interesse
url ='https://www.instagram.com/graphql/query/?query_hash=9dcf6e1a98bc7f6e92953d5a61027b98&variables={"id":"1697296","first":36}'
#first : 36 c'est les premieres images (un nombre au hasard)

r = requests.get(url)
json_data=json.loads(r.text)
#la ligne suivante permet d'avoir tous les nodes de la page
clean_data = json_data['data']['user']['edge_owner_to_timeline_media']['edges']#renseignement du chemin pris sur la page web de la resuete json

with open('instajson.txt', 'w', encoding="utf-8") as f:#ecriture dans un fichier
	for node in clean_data:
		f.write(str(node) + '\n\n' + " Node suivant: "  +'\n\n')#on ecris en chaine de caractere car c'est un dictionnaire}
		
		