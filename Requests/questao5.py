import requests
from bs4 import BeautifulSoup

def pesquisa(u):
    respPesq = requests.get(u)
    s = BeautifulSoup(respPesq.text, 'html.parser')
    return s.get_text()


def main():
    p = input('Palavra a ser buscada: ')
    u =(f'https://www.google.com.br/search?q={p}')

    c = pesquisa(u)
    print(c)


main()