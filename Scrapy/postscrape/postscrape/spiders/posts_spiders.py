# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:20:52 2020

@author: const
"""
import scrapy
import requests
import json

class PostsSpider(scrapy.Spider):
    name = 'posts'#nom de la propriete à utiliser dans le prompt

    start_urls = [ #toujours rajouter le s à la fin
            'https://blog.scrapinghub.com/'
    ]
    
    def parse(self, response):
         for post in response.css('div.post-item'):#boucle
             yield{#retire les balises
                 'title': post.css('.post-header h2 a::text')[0].get(),
                 'date': post.css('.post-header a::text')[1].get(),
                 'author': post.css('.post-header a::text')[2].get()
            }
             
        #ajout de code pour le parcours de plusieurs pages
         next_page = response.css('a.next-posts-link::attr(href)').get()#invocation du lien qui contient l'attribut(href)
         if next_page is not None: #assure qu'il y a une page suivante
            next_page = response.urljoin(next_page)#joindre la page suivante
            yield scrapy.Request(next_page, callback=self.parse)
             #title = post.css('.post-header h2 a::text')[0].get()
             #date = post.css('.post-header a::text')[1].get()
             #author = post.css('.post-header a::text')[2].get()
             #print(dict(title = title, date = date, author = author))
             


"""
Requete POST pour envoyer le fichier json
"""           
data = {"title": "Sur la route de ConstantinZOU", "date": "June 23, 2020 ", "author": "BAh prepare toi"}
r = requests.post("http://86.246.8.39:15490/documents", data = json.dumps(data))
print(r.text)

     
'''
response.css('title')
Out[1]: [<Selector xpath='descendant-or-self::title' data='<title>THE SCRAPINGHUB BLOG</title>'>]

response.css('title').get()
Out[3]: '<title>THE SCRAPINGHUB BLOG</title>'

 response.css('title::text').get()
Out[4]: 'THE SCRAPINGHUB BLOG'

response.css('h3::text')[1].get()
Out[7]: 'n  Crawl web data at scale without Bottlenecks or slowdowns.\n'

response.css('h3::text').getall()
Out[11]:
['Keep up to date with web scraping  and data tips...',
 'n  Crawl web data at scale without Bottlenecks or slowdowns.n',
 'Follow Us',
 'Popular Posts',
 'Recent Posts',
 'Categories',
 'Archives']

response.css('h3').getall()
Out[12]:
['<h3 id="hs_cos_wrapper_module_1577809707375810_title" class="hs_cos_wrapper form-title" data-hs-cos-general-type="widget_field" data-hs-cos-type="text">Keep up to date with web scraping  and data tips...</h3>',
 '<h3 style="text-align: center;"><a href="https://blog.scrapinghub.com/how-to-scrape-the-web-without-getting-blocked" rel=" noopener"><span style="font-size: 20px;">How to scrape the web without getting blocked</span></a></h3>',
 '<h3>\n  Crawl web data at scale without Bottlenecks or slowdowns.\n</h3>',
 '<h3>Follow Us</h3>',
 '<h3>Popular Posts</h3>',
 '<h3>Recent Posts</h3>',
 '<h3>Categories</h3>',
 '<h3>Archives</h3>']

 response.css('.blog-title').getall()
Out[15]: ['<div class="blog-title">\n  <a href="https://blog.scrapinghub.com">\n  \t<h1>THE SCRAPINGHUB BLOG</h1>\n    <h2 class="site-description">Turn Web Content Into Useful Data</h2>\n  </a>\n</div>']

 response.css('.blog-title h1').getall()
Out[19]: ['<h1>THE SCRAPINGHUB BLOG</h1>']

response.css('.blog-title h1::text').getall()
Out[20]: ['THE SCRAPINGHUB BLOG']

response.css('.blog-title h1::text')[0].getall()
Out[21]: ['THE SCRAPINGHUB BLOG']

response.css('a').get()
Out[26]: '<a href="https://blog.scrapinghub.com">\n  \t<h1>THE SCRAPINGHUB BLOG</h1>\n    <h2 class="site-description">Turn Web Content Into Useful Data</h2>\n  </a>'

response.css('a').getall()
Out[27]:
['<a href="https://blog.scrapinghub.com">\n  \t<h1>THE SCRAPINGHUB BLOG</h1>\n    <h2 class="site-description">Turn Web Content Into Useful Data</h2>\n  </a>',
 '<a href="https://blog.scrapinghub.com/extract-articles-at-scale-designing-a-web-scraping-solution" title="" class="hs-featured-image-link">\n<img src="https://cdn2.hubspot.net/hub/4367560/hubfs/Blog---Extract-articles-at-scale-april-2020-resize-v2.gif?width=830&amp;name=Blog---Extract-articles-at-scale-april-2020-resize-v2.gif" class="hs-featured-image" alt="">\n</a>',
 
..... 

'<a href="https://blog.scrapinghub.com/ ......
Prends tous les liens de la page

response.css('a')[0].get()
Out[28]: '<a href="https://blog.scrapinghub.com">\n  \t<h1>THE SCRAPINGHUB BLOG</h1>\n    <h2 class="site-description">Turn Web Content Into Useful Data</h2>\n  </a>'

response.css('.post-header a').get()
Out[29]: '<a href="https://blog.scrapinghub.com/extract-articles-at-scale-designing-a-web-scraping-solution">Custom crawling &amp; News API: designing a web scraping solution</a>'

 response.css('.post-header a::text')[1].get()
Out[31]: 'April 28, 2020 '

esponse.css('p::text').re(r'scraping')
Out[34]: ['scraping', 'scraping', 'scraping']

 response.css('p::text').re(r's\w+')
Out[35]:
['scraping',
 'sually',
 'sites',
 'standard',
 'some',
 'site',
 'scale',
 'so',
 'site',
 'so',
 'sn',
 'scale',
......

prends toutes les expressions commençant par le s
re : regular expressions

response.css('p::text').re(r'(\w+) you (\w+)')
Out[38]:
['API',
 'can',
 'If',
 'need',
 'challenges',
 'need',
 'once',
 'are',
 'allows',
 'to',
 'when',
 'extract']

response.xpath('//h3') 
prends le h3

[<Selector xpath='//h3' data='<h3 id="hs_cos_wrapper_module_1577809...'>,
 <Selector xpath='//h3' data='<h3 style="text-align: center;"><a hr...'>,

response.xpath('//h3/text()').extract()
Out[46]:
['Keep up to date with web scraping  and data tips...',
 '\n  Crawl web data at scale without Bottlenecks or slowdowns.\n',
 'Follow Us',
 'Popular Posts',
 'Recent Posts',
 'Categories',
 'Archives']

response.xpath('//h3/text()').getall()
Out[47]:
['Keep up to date with web scraping  and data tips...',
 '\n  Crawl web data at scale without Bottlenecks or slowdowns.\n',
 'Follow Us',
 'Popular Posts',
 'Recent Posts',
 'Categories',
 'Archives']

response.xpath('//*[@id="hs_cos_wrapper_module_1523032069834331"]/div/div/div/div/div[1]/div[2]/div[2]/div/span[2]/a/text()').extract()
Out[52]: ['Attila Tóth']

post = response.css('div.post-item')[0]

In [55]: post
Out[55]: <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' post-item ')]" data='<div class="post-item">\n<div class="h...'>

title = post.css('.post-header h2 a::text')[0].get()

In [57]: title
Out[57]: 'Custom crawling & News API: designing a web scraping solution'

In [58]: date = post.css('.post-header a::text')[1].get()

In [59]: date
Out[59]: 'April 28, 2020 '

In [60]: author = post.css('.post-header a::text')[2].get()

In [61]: author
Out[61]: 'Júlio César Batista'

for post in response.css('div.post-item'):
    ...:     title = post.css('.post-header h2 a::text')[0].get()
    ...:     date = post.css('.post-header a::text')[1].get()
    ...:     author = post.css('.post-header a::text')[2].get()
    ...:     print(dict(title = title, date = date, author = author))
    ...:
{'title': 'Custom crawling & News API: designing a web scraping solution', 'date': 'April 28, 2020 ', 'author': 'Júlio César Batista'}
{'title': 'Vehicle API (Beta): Extract Automotive Data at Scale', 'date': 'April 16, 2020 ', 'author': 'Attila Tóth'}
....
....



    start_urls = [ #toujours rajouter le s à la fin
        'https://blog.scrapinghub.com/page/1/', 
        'https://blog.scrapinghub.com/page/2/'  
    ]
        
    def parse(self, response):#creation d'un parseur
    #demembrement de l'adresse url, prends le numéro en fonction de la page ou on se trouve
        page = response.url.split('/')[-1]
        filename = 'posts-%s.html'% page
        with open(filename, 'wb') as f:
            f.write(response.body)#ecrit le corps du site en html
     
'''