import requests
from bs4 import BeautifulSoup

def tabela(u):
    respTab = requests.get(u)
    s = BeautifulSoup(respTab.text, 'html.parser')

    return s.find('Tabela de Classificação')

def main():
  
    c = tabela("https://ge.globo.com/sp/futebol/campeonato-paulista/")
    print(c)


main()