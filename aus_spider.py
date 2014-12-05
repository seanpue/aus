import scrapy

class DmozSpider(scrapy.Spider):
    name = "aus"
    allowed_domains = ["www.urdustudies.com"]
    start_urls = [
        "http://www.urdustudies.com"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
