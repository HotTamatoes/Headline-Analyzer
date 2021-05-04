import requests
from bs4 import BeautifulSoup

import mysql.connector

# website_analyzed is the name for the website 
website_analyzed = ""
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="PZZwsmapE4-Uk:6"
)
mycursor = mydb.cursor()
sqlFormula = ""

#URL to be scraped
url_to_scrape = 'https://www.politico.com/magazine/story/1'
# Load html's plain data into a variable
# NOTE: .text returned a string with bad encoding (maybe cp1252) -- .content.decode('utf-8') 
#       returns HTML as bytes (.content), then converts them to string with 
#       proper encoding (.decode('utf-8'))
#       SOURCE: https://stackoverflow.com/a/65027863
plain_html_text = requests.get(url_to_scrape).content.decode('utf-8')
#parse the data
soup = BeautifulSoup(plain_html_text, 'html.parser')
#get list of all articles
articles = soup.find_all('article')

def create_tuple():
    url_list = create_url_list()
    scraped_info = []
    for url in url_list:
        plain_text_html = requests.get(url).content.decode('utf-8')
        soup = BeautifulSoup(plain_text_html, 'html.parser')
        articles = soup.find_all('article')

        for article in articles:
            #print(get_authors(article))
            article_tuple = tuple((get_category(article), get_title(article), get_authors(article),
                                    get_link(article), get_subheader(article), get_date_time(article)))
            scraped_info.append(article_tuple)

    #print(len(scraped_info))
    return scraped_info

## Returns list of urls comprising of all politico archives
## TODO: try/except for page 348 links
def create_url_list():
    
    url_list = []
    url = 'https://www.politico.com/magazine/story/{}'
    pages = 686
    for i in range(1, 2):
        try:
            url_list.append(url.format(i))
        except:
            print('Ran into problem with page: ' + i + '\n')
    return url_list    


## Prints out catagory of article
def get_category(article):
    if (len(article.find_all("p", class_ = "category")) == 1):
        return article.find_all("p", class_ = "category")[0].get_text()

## Prints out subheader for all article in articles 
def get_subheader(article):
    if (len(article.find_all("p", class_ = "subhead")) == 1):
        return (article.find_all("p", class_ = "subhead")[0].string)

## Prints out link for article
## TODO: try/except for page 348 links
def get_link(article):
    return article.h3.get('href')

def get_title(article):
    return article.h3.string

## Prints out authors of article
## TODO: store as "author1, author2"
def get_authors(article):
    span_list = article.footer.find_all("span", class_ = "vcard")
    authors = ""
    for name in span_list:
        authors = authors + ", " + str(name.string)
    return authors[2:]

def get_date_time(article):
    ## returns as MM/DD/YY  00:00 XM EST
    return article.time.string
    ## returns as YYYY-MM-DDT00:00-0000 (not sure exactly what format is -- run to check)
    # return article.time.get('datetime')