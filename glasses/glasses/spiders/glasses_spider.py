# -*- coding: utf-8 -*-
import scrapy
import logging


class GlasssesSpiderSpider(scrapy.Spider):
    name = 'glasses_spider'
    allowed_domains = ['wwww.glassesshop.com']
    

    def start_request(self):
        yield scrapy.Request(url='https://www.glassesshop.com/bestsellers', callback=self.parse, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'})

    def parse(self, response):
        glasses = response.xpath("//div[contains(@class, 'm-p-product')]")
        for glass in glasses:

                yield {
                    'title': title.xpath(".//div[@class='row']/p[contains(@class, 'pname')]/a/text()").get(),
                    'url': url.xpath(".//div[@class='pimg default-image-front']/a/@href").get(),
                    'price': product.xpath(".//div[@class='row']/div[contains(@class, 'pprice')]/span/text()").get(),
                    'image_link': image.xpath(".//div[@class='pimg default-image-front']/a/img[1]/@src").get(),
                    'User-Agent': response.request.headers['User-Agent']
                    }
        next_page = response.xpath(".//ul[@class='pagination']/li[7]/a/@href").get()
        if next_page:
            yield  scrapy.Request(url=next_page, callback=self.parse, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'})
                    
        
