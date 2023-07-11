import requests
from bs4 import BeautifulSoup

u = 'https://stackoverflow.com/'

respTag = requests.get(u).content

s = BeautifulSoup(respTag, 'html.parser' )

for tag in soup.find_all('a'):
    if tag is None:
        continue
    link = tag.get('href')
    print(link)

