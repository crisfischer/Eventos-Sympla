# -*- coding: utf-8 -*-
import scrapy


class EventosSpider(scrapy.Spider):
    name = 'eventos'
    # start_urls = ['https://www.sympla.com.br/eventos/florianopolis-sc/']
    URL = 'https://www.sympla.com.br/eventos/florianopolis-sc/'

    def start_requests(self):
        yield scrapy.Request(url=self.URL, callback=self.parse)

    def parse(self, response):
        divs = response.xpath('//div[@id="events-grid"]/div')
        for div in divs:
            link = div.xpath('./a/@href').extract_first()
            title = div.xpath('.//p/text()').extract_first()
            date = self.get_date(div)
            hour = div.xpath('.//a/div[4]/div[2]/text()').extract()[1].strip()
            local = div.xpath('.//div[@class="uppercase line"]/p/text()').extract_first()

            yield {
                'link': link,
                'title': title,
                'date': date,
                'hour' :hour,
                'local':local
            }

    def get_date(self, div):
        mes = div.xpath('//*[@id="events-grid"]/div[1]/a/div[3]/div[1]/text()').extract_first().strip()
        dia = div.xpath('//*[@id="events-grid"]/div[1]/a/div[3]/div[2]/text()').extract_first().strip()
        return mes +" "+ dia
