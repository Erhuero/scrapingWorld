# -*- coding: utf-8 -*-
import scrapy
import json
from datetime import datetime
import requests
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import schedule
from scrapy.crawler import CrawlerProcess
import csv

class GoldenSpider(scrapy.Spider):
    name = 'golden'
    allowed_domains = ['bdor.fr/cours-or']
    start_urls = ['https://www.bdor.fr/cours-or']
    

    def parse(self, response):
        #prix = response.xpath('//td[@class="atelierEval"]')
        #print(prix)
        contenu = response.xpath('//tr[@class="ligneProdCO"]')
        #print(contenu)
        #print(len(contenu))
        content = "["
        #golden_url=""
        golden_url = self.start_urls
        date_ref=datetime.today().strftime('%Y%m%d%H%M%S')

        for curseur in contenu:
          
          titre = curseur.xpath('.//td[@class="anneeEval nomCO"]/a/p/text()').extract_first()
          titre_r = titre.replace("\u00e9", "e")
          
          prix = curseur.xpath('.//td[@class="atelierEval"]/text()').extract_first()
          prix_float= prix.replace("€", "").replace(" ", "")
          prix_float_r= prix_float.replace(",", ".")
          prix_f=float(prix_float_r)
          #print(prix_f)
          #date = curseur.xpath('//div[@class="tabCoursComplet"]/p/strong/text()').extract_first()
          #date_ref=datetime.today().strftime('%Y%m%d%H%M%S')
          #golden_url = self.start_urls

          #data2 = data "{'url':'", golden_url  }" 
          #print(golden_url)

          
          #json.dumps(data)
          #data ="["
          #print(golden_url)
 
          #varTest =  "{'url'": golden_url, "'libelle'" : titre_r, ""'prix' : prix_f, 'date' : date_ref}"
          
 
          #varTest =  {'libelle' : titre_r, 'prix' : prix_f, 'date' : date_ref}
          varTest =  {'libelle' : titre_r, 'prix' : prix_f}

          
          #print(titre_r)
          #print(prix_f)
          #print(varTest)
          content += json.dumps(varTest)#dumps convertit le tout en string

        
          content+=","
        content=content[0:len(content)-1]#suppression du dernier commentaire
        data = '{"url":"' + golden_url[0] + '", "date":"' + date_ref  + '", "variations": ' + content


        
        data+="]}"

        print(data)

        print(json.loads(data))
        r = requests.post("http://86.246.8.39:15489/variations", json=json.loads(data))#json= permet d'envoyer le fichier en format json
        print(r.text)

      
"""
    schedule.every().day.at("14:30").do(parse)

    while True:
      schedule.run_pending()
      time.sleep(1)
"""
process= CrawlerProcess()
process.crawl(GoldenSpider)
process.start()

#schedule.every().day.at("14:30").do(GoldenSpider)
schedule.every().minute.do(GoldenSpider)

while True:
  schedule.run_pending()
  time.sleep(1)


