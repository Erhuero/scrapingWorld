# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class NewItem(scrapy.Item):
    # define the fields for your item here like:
    #name = scrapy.Field()
    
    #Main Fields
    main_headline = Field()
    headline = Field()
    
    #Champs separes
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
    
    #Champs de localisation
    #location = Field()
    
class TestItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()