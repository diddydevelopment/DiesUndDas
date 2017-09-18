import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.jimmyjazz.com/mens/footwear/puma-clyde-coogi/364907-01?color=Multi-Color')

soup = BeautifulSoup(html.text,'lxml')

available_sizes = []
unavailable_sizes = []

for size in soup.find_all('a',class_='box'):
    item_id = size.contents[0]
    #print(item_id)
    if 'piunavailable' in size.get('class'):
        unavailable_sizes.append(item_id)
    else:
        available_sizes.append(item_id)

print('available sizes: ',available_sizes)
print('unavailable sizes: ',unavailable_sizes)
