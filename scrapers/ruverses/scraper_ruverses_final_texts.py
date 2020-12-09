import scrapy
import json
import re
# ИСПРАВИТЬ <em> в https://ruverses.com/konstantin-simonov/i-want-to-say-to-you-you-are-my-wife/
# <div> в https://ruverses.com/vladislav-khodasevich/a-ballad/3645/
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    file = open("./data/thrd_lvl_links_ruverses.json", "r")
    j = json.load(file)
    start_urls = []
    for i in j:
        start_urls.append(i["text"])
    # start_urls = list(filter(lambda x: "#" not in x, start_urls))

    def parse(self, response):
        # for quote in response.css('div.rudescr'):
        article = []
        original = []
        string = None
        for quote in response.css('div.article > p'):
            string = quote.css("p").get()
            string = re.sub(r"<em>.*?</em>", r"", string)
            string = re.sub(r"<.*?>", r"", string)
            string = re.sub(r"\r\n", r"\n", string)
            article.append(string)
        string = None
        for quote in response.css('div.original > p'):
            string = quote.css("p").get()
            string = re.sub(r"<em>.*?</em>", r"", string)
            string = re.sub(r"<.*?>", r"", string)
            string = re.sub(r"\r\n", r"\n", string)
            original.append(string)
        yield {
            "article": "\n".join(article),
            "original": "\n".join(original),
            "text": str(response.css("div.rudescr::text").get()),
            "url": response.url
        }