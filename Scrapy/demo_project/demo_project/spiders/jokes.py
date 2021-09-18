import scrapy
from demo_project.items import JokeItem
from scrapy.loader import ItemLoader


class JokesSpide(scrapy.Spider):
    name='jokes'

    start_urls = ["http://www.laughfactory.com/jokes/family-jokes"]

    def parse(self, response): #methode self comme premier argument
        for joke in response.xpath("//div[@class='jokes']"):#on peut parser un fichier css en remplaçant xpath par css
            l = ItemLoader(item = JokeItem(), selector = joke)#instanciation des champs
            l.add_xpath('joke_text', ".//div[@class = 'joke-text']/p")
            yield l.load_item()#meme chose qu'en dessous, mais on utilise les input/output
            """
            yield {#dictionnaire avec joke_text comme cle et le selecteur joke 
                'joke_text': joke.xpath(".//div[@class = 'joke-text']/p").extract_first()
            }
            """
            
        next_page = response.xpath("//li[@class = 'next']/a/@href").extract_first()#contient les attributs des liens des pages suivantes
        if next_page is not None:#verifie si la page suivante n'est pas vide
            next_page_link = response.urljoin(next_page)#contact le site web suivant
            yield scrapy.Request(url = next_page_link, callback= self.parse)
        