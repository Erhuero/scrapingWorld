# -*- coding: utf-8 -*-
"""
Created on Fri May  1 11:19:35 2020

@author: const

conda create -n ScrapyEnvironment pour creer un environnement
conda activate ScrapyEnvironment pour activer l'environnement dans le prompt
conda install -c conda-forge scrapy=1.6.0 installation de la version 1.6 car > ne fonctionne pas
"""
import scrapy

class FirstSpider(scrapy.Spider):
    name = "FirstSpider"
    
    def start_requests(self): #retourne la liste des requêtes etc
        urls = ['http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/', #page suivante
        ]
        for url in urls :
            yield scrapy.Request(url=url, callback=self.parse)#sert à enlever des parentheses
    def parse(self, response):
        page = response.url.split("/")[-2]#selcetionne un morceau de l'adressse
        filename = 'quotes-%s.html' % page
        with open (filename, 'wb') as f:
                   f.write(response.body)#retour du contenu du scrap
        self.log('Saved file %s' % filename)
                  
                   
                 
                

