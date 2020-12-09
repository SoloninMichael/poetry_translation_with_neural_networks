import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://ruverses.com/",
        ]

    def parse(self, response):
        for quote in response.css('div.article.content.mainpage > div.outer > ul > li'):
            # section = quote.css("a::attr(href)").get()
            
            # print("https://ruverses.com" + quote.css("a::attr(href)").get())
            yield {
                'text': "https://ruverses.com" + quote.css("a::attr(href)").get()
            }