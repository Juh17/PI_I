import requests
from bs4 import BeautifulSoup

u = 'https://stackoverflow.com/'

respTag = requests.get(u).content

s = BeautifulSoup(respTag, 'html.parser' )

t = input("Insira a tag que você deseja localiza: ")


for j in soup.find_all(t):
    print(j)

