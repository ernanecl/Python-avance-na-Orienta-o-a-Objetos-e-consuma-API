import requests
import json

url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    attributes = ((str(json_data.values())).removeprefix('dict_values([')).removesuffix('])')
    #lib = dict(attributes)

    print(type(attributes))
    print(attributes)
    #print(list(json_data.values()))


else:
    print(f'request not found')

explanation = {
'Atributo': 'Descrição',
'code': 'Código da moeda (USD - Dólar Americano)',
'codein': 'Código da moeda de referência (BRL - Real Brasileiro)',
'name': 'Nome da moeda (Dólar Americano/Real Brasileiro)',
'high': 'Valor mais alto durante o período',
'low': 'Valor mais baixo durante o período',
'varBid': 'Variação do lance (oferta)',
'pctChange': 'Percentual de mudança',
'bid': 'Preço de compra (lance)',
'ask': 'Preço de venda (oferta)',
'timestamp': 'Carimbo de data/hora UNIX (timestamp)',
'create_date': 'Data e hora da criação do registro'
}



