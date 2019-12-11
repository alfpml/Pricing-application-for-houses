from scrapy import Spider
from ..items import GethousesItem
from .config import API_KEY

class houseCrawl(Spider):
    name="house"
    url_link="https://www.idealista.com/venta-viviendas/madrid/moncloa/aravaca/pagina-2.htm"
    page_number=5

    start_urls=['http://api.scraperapi.com/?api_key='+ API_KEY + '&url=' + url_link + '&render=true']


    def parse(self,response):
        houses=response.css("div.item-info-container")
        items=GethousesItem()
        for house in houses:
            items["title"]=movie.css('.title::text').extract()

            yield items

    
        next_page_url = "https://www.idealista.com/venta-viviendas/madrid/moncloa/aravaca/pagina-"+str(self.page_number)+".htm"
        next_page='http://api.scraperapi.com/?api_key='+API_KEY +'&url='+ next_page_url+'&render=true'

        if self.page_number<=5:
            self.page_number+=1
            yield response.follow(next_page,callback=self.parse)
