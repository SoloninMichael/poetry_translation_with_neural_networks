import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    file = open("./data/scnd_lvl_links_ruverses.json", "r")
    j = json.load(file)
    start_urls = []
    for i in j:
        start_urls.append(i["text"])
    start_urls = list(filter(lambda x: "#" not in x, start_urls))

    def parse(self, response):
        if len(response.css("div.original")) != 0:
            #there are no additional links
            yield {
                'text': response.url
            }
        else:
            for quote in response.css('div.content.article > ul > li'):
                yield {
                    'text': "https://ruverses.com" + quote.css("a::attr(href)").get()
                }