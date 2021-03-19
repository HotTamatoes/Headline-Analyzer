## SCRAPER FILE -- write to SQL

import scrapy
from scrapy import Request

from dateutil.parser import parse


class WpostScraperSpider(scrapy.Spider):
    name = 'wpost_scraper'
    allowed_domains = ['wsj.com']

    def start_requests(self):
        url = 'https://www.wsj.com/news/archive/{}'
        for year in range(1995, 2000):
            str i = url.format(year)
        