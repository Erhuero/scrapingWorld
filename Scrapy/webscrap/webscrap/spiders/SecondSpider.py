# -*- coding: utf-8 -*-

"""
Created on Fri May  1 16:53:42 2020

@author: const

travail avec le JSON, structures interchangeables
python -m pip install -U prompt-toolkit~=2.0 pour adapter la version

fetch("https:// xxxxxxxx ")
view(response)
"""

"""
#reprise du code d'une page web avec fetch( ) , view(response) print(response.text)

class SecondSpider(scrapy.Spider):#initialiser la classe
    name = "SecondSpider"
    
    start_urls = ['http://supe rdatascience.com/artificial-intelligence']
    def parse(self, response)
    
  """  
import scrapy

from webscrap.items import NewItem
#from scrapy.selector import Selector

class SecondSpider(scrapy.Spider):
    name = 'secondspider'
    #creation de listes de domaines de sites internet
    allowed_domains = ['www.superdatascience.com']
    start_urls = ['https://superdatascience.com']
    
    #debut de parcours des sites web
    def parse(self, response):
        item = NewItem()#instanciation d'un objet
        item['main_headline'] = response.xpath('//div/h4/text()').get()#informations extraits utilisant le selecteur span
        item['headline'] = response.xpath('//title/text()').extract()
        item['url'] = response.url
        item['project'] = self.settings.get('BOT_NAME')#utilisation de item pour avoir le nom du projet
        item['spider']=self.name#avoir le nom de l'araignee
        
        return item
        
    
    