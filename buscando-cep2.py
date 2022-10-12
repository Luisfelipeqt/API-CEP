import requests
import pprint
import pandas 
from display import display


uf = "MA"
cidade = "São Luis"
endereco = "Rua 2"

link = f"https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/"
requisicao = requests.get(link)
print(requisicao)

dic_requicicao = requisicao.json()
tabela = pandas.DataFrame(dic_requicicao)
display(tabela)


print(dic_requicicao)

pprint.pprint(dic_requicicao)