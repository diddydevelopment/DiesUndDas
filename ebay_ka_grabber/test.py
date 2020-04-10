import requests
import urllib.request
import time
from bs4 import BeautifulSoup


# https://www.ebay-kleinanzeigen.de/s-tamron-sp-24-70-2.8-vc-nikon/k0

base_url = 'https://www.ebay-kleinanzeigen.de'
search_term = 'tamron sp 24 70 2.8 vc nikon'

search_term_url = search_term.replace(' ', '-')

url = base_url+'/s-'+search_term_url+'/k0'

html = requests.get(url).text

bs = BeautifulSoup(html, 'html.parser')

articles = bs.findAll('article')

id = articles[0]['data-adid']
href = articles[0].find('a')['href']
article_html = requests.get(base_url+href).text

