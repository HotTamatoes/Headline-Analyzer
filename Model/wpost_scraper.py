## SCRAPER FILE -- write to SQL

import scrapy
from scrapy import Request

from dateutil.parser import parse


class WpostScraperSpider(scrapy.Spider):
    name = 'wpost_scraper' # internet scraper
    allowed_domains = ['wsj.com'] # news platform being scraped
    list_date = [] # list of dates (used for scraping from wsj.com)

    # fills list_date with strings of the following format yyyy/mm/dd Ex: "2020/01/04"
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
                        date = year + "/" + str(month).zfill(2) + "/" + str(day).zfill(2)
                        list_date.add(date)
                else:
                    for day in range(1, 31 - month%2):
                        date = year + "/" + str(month).zfill(2) + "/" + str(day).zfill(2)
                        list_date.add(date)

    # reads the information from the website
    def start_requests(self):
        url = 'https://www.wsj.com/news/archive/{}'
        list_date = make_list()
        for i in range(list_date.size()):
            yield Request(url.format(list_date(i)))

    def parse(self, response):
        for news in response.css('ul.items>li.row'):
            yield {
                'title': news.css('a::text').extract_first('').strip(),
                'link': response.urljoin(news.css('a::attr(href)').extract_first()),
                'published_date': parse(news.css('div.date::text').extract_first()).strftime('%Y-%m-%d'),
            }

            next_page = response.css('a.next::attr(href)').extract_first()
            if next_page:
                yield Request(response.urljoin(next_page))
        