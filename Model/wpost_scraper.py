## SCRAPER FILE -- write to SQL

import scrapy
from scrapy import Request

from dateutil.parser import parse


class WpostScraperSpider(scrapy.Spider):
    name = 'wpost_scraper'
    allowed_domains = ['wsj.com']
    list_date = []

    def make_list():
        for year in range(1995, 2020):
            for month in range(1,12):
                if (month == 2):
                    if (year%4 == 0):
                        for day in range(1, 29):
                            date = year + "/" + str(month).zfill(2) + "/" + str(day).zfill(2)
                            list_date.add(date)
                    else:
                        for day in range(1, 28):
                            date = year + "/" + str(month).zfill(2) + "/" + str(day).zfill(2)
                            list_date.add(date)
                elif (month < 8):
                    for day in range(1, 30 + month%2):
                        str date = year + "/" + str(month).zfill(2) + "/" + str(day).zfill(2)
                        list_date.add(date)
                else:
                    for day in range(1, 31 - month%2):
                        str date = year + "/" + str(month).zfill(2) + "/" + str(day).zfill(2)
                        list_date.add(date)

    def start_requests(self):
        url = 'https://www.wsj.com/news/archive/{}'
        list_date = make_list()
        for i in range(list_date.size()):
            yield Request(url.format(list_date(i)))
        