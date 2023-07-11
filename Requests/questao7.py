import requests

c = input("CEP: ")
u = f'https://viacep.com.br/ws/{c}/json/'
e = requests.get(u)
print(e.json())
