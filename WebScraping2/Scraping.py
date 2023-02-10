import requests
from bs4 import BeautifulSoup
import pandas as pd 

url_base ='https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja?')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default'})

lista = []

for produto in produtos:
     titulo = produto.find('h2', attrs={'class':'ui-search-item__title shops__item-title'})
 
     reais = produto.find('span', attrs={'class':'price-tag-fraction'})

     link = produto.find('a', attrs={'class':'ui-search-link'})
 
     #print(produto.prettify())
     #print('Titulo do produto:', titulo.text)
     #print('Link do produto:', link['href'])
     #print('Preço do produto: R$', reais.text)
     #print('\n')
     
     lista.append([titulo, reais, link['href']])

lista_final = pd.DataFrame(lista, columns=['titulo', 'reais', 'link']) 

lista_final.to_excel('Lista_mercado_livre.xlsx', index=False)
print('Dados Extraido com sucesso..')
  