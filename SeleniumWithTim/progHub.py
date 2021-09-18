#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver#selenium est une bibliotheque qui permet d'appeler l'api de notre browser

class ProgHubParser(object):

	def __init__(self, driver, lang):
		self.driver=driver
		self.lang=lang

	def parse(self):
		self.go_to_tests_page()
		

	def go_to_tests_page(self):
		self.driver.get("https://proghub.ru/tests")
		slide_elems  =  self.driver.find_elements_by_class_name("carousel__card")#reprend les menus de la page en selectionnant les classes, bien preciser elements au pluriel

		for elem in slide_elems:#avoir la liste de tous les elements de la page en collectant avec une boucle for
			lang_link = elem.get_attribute("href")#affiche l'element, la methode speciale est get_attribute

			if self.lang in lang_link:
				language = lang_link.split("/")[-1]#decoupage d'adresse en plusieurs morceaux
				self.driver.get("https://proghub.ru/q/random/t" + language)
				break
"""
			l= "https://proghub.ru/t/oop-basic"
>>> l.split("/")[-1] 
#reprise de la dernoere adresse avec un -1
"""

def main():
	driver = webdriver.Chrome()
	#driver.get("https://proghub.ru/")
	parser = ProgHubParser(driver, "python")
	parser.parse()

	#btn_elem = driver.find_element_by_class_name("home__meeting_banner_action_btn")#element d'information sur le bouton
	#btn_elem = driver.findElement(By.linkText("home__meeting_banner_action_btn"))
	#btn_elem.click()

	#titre = driver.find_element_by_tag_name("h2")
	#print(titre.text)

	#print(btn_elem)
	time.sleep(5)#arreter la page pendant quelques secondes pour qu'il aie le temps de se connecter

if __name__ == '__main__':#connexion au parser
	main()