# import the packages
from getAnimePics.items import GetanimepicsItem
import datetime
import scrapy

class CoverSpider(scrapy.Spider):
    name = "pyimagesearch-cover-spider"
    start_urls = ["https://gelbooru.com/index.php?page=post&s=list&tags=solo+tomoe_gozen_%28fate%2Fgrand_order%29+rating%3Asafe&pid=84"] 

    def parse(self, response):
        #For every thumbnail, extract the image link from under the span a attribute
        for url in response.xpath(""):
            yield scrapy.Request(url.css("span a::attr(href)").extract_first(), self.parse_images)
        #url = response.css("span a::attr(href)").extract()
    
    def parse_images(self, response):
        url = response.css("img::atr(src)").extract()
        for item in zip(url):
            scraped_info = {
                'image_urls' : [item[0]]
            }
        
        yield scraped_info

            


