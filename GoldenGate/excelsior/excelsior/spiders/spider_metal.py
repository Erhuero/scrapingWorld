# -*- coding: utf-8 -*-
"""
Created on Sun May 17 23:36:24 2020

@author: const
"""
import scrapy

class PostsSpider(scrapy.Spider):
    name = 'gold'#nom de la propriete à utiliser dans le prompt

    start_urls = [ #toujours rajouter le s à la fin
            #'https://www.bdor.fr/cours-or'
            'https://www.scrapinghub.com/'
    ]
    
    def parse(self, response):
        
        for parse in response.xpath('//*[@id="colonne_1200"]/div[8]/div[1]'):
            yield{
                'montant1' : parse.xpath('//*[@id="colonne_1200"]/div[8]/div[1]/table/tbody/tr[1]/td[2]').extract(),
                'montant' : parse.xpath('//*[@id="colonne_1200"]/div[8]/div[1]/table/tbody/tr[5]/td[2]').extract()
                }
            