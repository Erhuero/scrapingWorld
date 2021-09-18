import scrapy

class RedditSpider(scrapy.Spider):
    name= "reddit"
    start_urls = ["https://www.reddit.com/r/cats/"]

    def parse(self, response):
        links = response.xpath("//img/@src")#prends les liens dans les pages
        html = ""

        for link in links:#acces au texte dans les liens
            url=link.get()#retourne l'url en chaine de caracteres

            if any(extension in url for extension in [".jpg", ".gif", ".png"]):
                html += """<a href="{url}"
                target = "_blank">
                <img src="{url}" height="33%" width = "33%"/>
                <a/>""".format(url=url)
#les {} nous permettent de construire chaque lien dynamiquement
                with open("frontpage.html", "a") as page:
                    page.write(html)
                    page.close()