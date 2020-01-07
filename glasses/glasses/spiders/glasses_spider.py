# -*- coding: utf-8 -*-
import scrapy
import logging


class GlasssesSpiderSpider(scrapy.Spider):
    name = 'glasses_spider'
    allowed_domains = ['www.glassesshop.com']
    

    def start_requests(self):
        yield scrapy.Request(url='https://www.glassesshop.com/bestsellers', callback=self.parse, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'})

    def parse(self, response):
        glasses = response.xpath("//div[contains(@class, 'm-p-product')]")
        for glass in glasses:

                yield {
                    'title': glass.xpath(".//div[@class='row']/p[contains(@class, 'pname')]/a/text()").get(),
                    'url': glass.xpath(".//div[@class='pimg default-image-front']/a/@href").get(),
                    'price': glass.xpath(".//div[@class='row']/div[contains(@class, 'pprice')]/span/text()").get(),
                    'image_link': glass.xpath(".//div[@class='pimg default-image-front']/a/img[1]/@src").get(),
                    'user-agent': response.request.headers.get('User-Agent').decode('utf-8')
                    }
        next_page = response.xpath("//a[@rel='next']/@href").get()
        if next_page:
            yield  scrapy.Request(url=next_page, callback=self.parse, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'})
