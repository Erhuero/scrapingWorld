import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        #print(response.url)
        #print(response.status)

        all_the_books = response.xpath('//article')
        
        print(len(all_the_books))
        for book in all_the_books:

            

            """
            title = book.xpath('.//h3/a/@title').extract_first()
            price = book.xpath('.//div[@class="product_price"]/p[@class="price_color"]/text()').extract_first()
            image_url = self.start_urls[0] + book.xpath('.//a/img/@src').extract_first()
            """
            book_url = self.start_urls[0] + book.xpath('.//div[@class="image_container"]/a/@href').extract_first()
            print(book_url)
                

            #print(title)
            #print(price)
            #print(image_url)
            #print(book_url)
            """
            yield {
                'Title' : title,
                'Price' : price,
                'Image URL' : image_url,
                'Book URL' : book_url
            }
            """