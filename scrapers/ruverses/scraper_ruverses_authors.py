import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # with open("ruverses_1lvl.txt", "r") as file:
    #     text = file.read()
    # start_urls = list(filter(None, text.split("\n")))
    # print(start_urls[-5:])
    # exit()
    file = open("./data/frst_lvl_links_ruverses.json", "r")
    j = json.load(file)
    start_urls = []
    for i in j:
        start_urls.append(i["text"])

    def parse(self, response):
    # with open("ruverses_2lvl.txt", "w") as file:
        for quote in response.css('div.article.content > div.outer > ul > li'):
            section = quote.css("a::attr(href)").get()
            # file.write("https://ruverses.com" + section + "\n")
            
            yield {
                'text': "https://ruverses.com" + quote.css("a::attr(href)").get()
            }