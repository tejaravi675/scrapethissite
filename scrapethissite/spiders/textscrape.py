import scrapy


class TextscrapeSpider(scrapy.Spider):
    name = 'textscrape'
    allowed_domains = ['www.scrapethissite.com']
    start_urls = ['http://www.scrapethissite.com/pages/']

    def parse(self, response):
        for text in response.xpath("//div[@class='page']"):
            yield {
                'title' : text.xpath(".//a/text()").get(),
                'text' : text.xpath(".//p/text()").get().strip()
            }
