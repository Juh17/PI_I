import requests 
import requests_cache
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def palavra_chave(c, t):
    array = []

    for i in range(len(t)):
        if t[i:i+len(c)] == c:
            ini = max(0, i - 10)
            fim = min(len(t), i+len(c) + 10)
            cont = t[ini:fim]
            array.append(cont)

    return array

class localizar_links:
    def iniciar(self, start_url, max_depth):
        self.pag_vis = []
        self.start_url = start_url
        self.max_depth = max_depth
        self.session = None
        self.references = {}


    def obter(self, u):
        s = self.get_session()
        resultado = s.get(u)
        soup = BeautifulSoup(resultado.content, 'html.parser')

        l = []
        for link in soup.find_all("a"):
            h = link.get('href')

            if h is not None:
                url_abs = self.url_abs(href, res.url)

                if url_abs not in self.pag_vis:
                    l.append(url_abs)
                if url_abs not in self.references:
                    self.references[url_abs] = 0

                self.references[url_abs] += 1
                        
        return l

    def armazenar_sessoes(self): 
        if not self.session:
            requests_cache.install_cache('cache')
            self.session = requests_cache.CachedSession()
        return self.session

    def url_abs(self, u, base):
        return urljoin(base, u)

    def pesquisa(self, u=None, depth=0):
        if not u:
            u = self.start_url
        if depth > self.max_depth:
            return [] 
      
        
        l = self.obter(u)
        self.pag_vis.append(url)
        links_em_ordem = []
        for link in sorted(l, c=lambda j: self.references[j], reverse=True):
            if link not in self.pag_vis:
                links_em_ordem.append(link)
                links_em_ordem.extend(self.search(link, depth+1))

        return links_em_ordem


# url = "http://127.0.0.1:5500/Buscador/Home.html"
u = input("URL: ")
c = input("Palavra-chave: ")
depthStr = input("Profundidade: ")
depth = int(depthStr)

findLinks = localizar_links(u, depth)
l = findLinks.search()

for pagina in findLinks.pag_vis:
    resultado = requests.get(pagina)
    soup = BeautifulSoup(resultado.text, 'html.parser')
    t = soup.get_text()
    ocorrencias = palavra_chave(c, t)


    print(f"\nLink da página: {pagina}")
    print("Contexto: ")
    for o in ocorrencias:
        print(f"- {o}")
 

    print(f"Quantidade de links referenciados: {findLinks.references[pagina]}")