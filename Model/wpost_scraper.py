## SCRAPER FILE -- write to SQL

import scrapy
from scrapy import Request

from dateutil.parser import parse

# To run the scraper
# scrapy runspider wpost_scraper.py -o wpost_scraper.csv
# scrapy runspider cnet_scraper.py -o cnet_scraper.json


class WpostScraperSpider(scrapy.Spider):
    
    print("TEST 1")
    name = 'wpost_scraper' # internet scraper
    allowed_domains = ['wsj.com'] # news platform being scraped
    list_date = ["2020/01/01"] # list of dates (used for scraping from wsj.com)

    # fills list_date with strings of the following format yyyy/mm/dd Ex: "2020/01/04"
    def make_list():
        print("TEST 2")
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
        print("TEST 3")
        url = 'https://www.wsj.com/news/archive/{}'
        # list_date = make_list()  #TODO: remove this when total
        for i in range(list_date.size()):
            # yield Request(url.format(list_date(i)))
            print(url.format(list_date(i)))

## NEEDS CHANGING
    def parse(self, response):
        for news in response.css('ol.WSJTheme--list-reset--3pR-r52l>article.WSJTheme--story--XB4V2mLz WSJTheme--padding-top-large--2v7uyj-o styles--padding-top-large--3rrHKJPO WSJTheme--padding-bottom-large--2lt6ga_1 styles--padding-bottom-large--2vWCTk2s WSJTheme--border-bottom--s4hYCt0s '):
            print("TEST")
            yield {
                'type': news.css('div.WSJTheme--articleType--34Gt-vdG>span').extract_first('').strip(),
                'link': response.urljoin(news.css('a::attr(href)').extract_first()),
                'title':news.css('a::text').extract_first('').strip(),

                # 'title': news.css('a::text').extract_first('').strip(),
                # 'link': response.urljoin(news.css('a::attr(href)').extract_first()),
                # 'published_date': parse(news.css('div.date::text').extract_first()).strftime('%Y-%m-%d'),
            }

            # next_page = response.css('a.next::attr(href)').extract_first()
            # if next_page:
            #     yield Request(response.urljoin(next_page))


## TESTING


        