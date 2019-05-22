import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions
from cloudant.client import CouchDB

natural_language_understanding = NaturalLanguageUnderstandingV1(
  iam_apikey='{api_key}}',
  version='2018-09-21')

client = CouchDB("{user}", "{pass}", url='{url_connection}', connect=True)
session = client.session()
print('Username: {0}'.format(session['userCtx']['name']))
print('Databases: {0}'.format(client.all_dbs()))

db_entidades = client['entidades']

t = 'A IBM é uma empresa multinacional com escritório na cidade de São Paulo. Nesta empresa trabalham diversas pessoas. Entre elas, o João da Silva e a Maria do Carmo.'
response = natural_language_understanding.analyze(
  text=t,
  language='pt',
  features=Features(
    entities=EntitiesOptions())).get_result()

response['input_text'] = t
my_doc = db_entidades.create_document(response)
if my_doc.exists():
    print('Resultado armazenado com sucesso')
#print(json.dumps(response, indent=2))

t = 'O jogador de futebol Zezé foi o responsável pelo campeonato do Fluminense. Hoje o Rio de Janeiro está em festa!'
response = natural_language_understanding.analyze(
  text=t,
  language='pt',
  features=Features(
    entities=EntitiesOptions())).get_result()

response['input_text'] = t
my_doc = db_entidades.create_document(response)
if my_doc.exists():
    print('Resultado armazenado com sucesso')
#print(json.dumps(response, indent=2))

client.disconnect()