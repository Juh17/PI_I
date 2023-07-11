import requests
from bs4 import BeautifulSoup

u = input("Insira a página a ser buscada: ")
x = input("Insira um determinado termo a ser buscado na página informada: ")

respTag = requests.get(u)
s = BeautifulSoup(respTag.content, 'html.parser')

t = soup.get_text()

for i in range(len(t1)):
    if t1[i:i+len(term)] == term:
        i = max(0, i - 20)
        f = min(len(t1), i + len(term) + 20)
        y = t1[i:f]
        print(y)