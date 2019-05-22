import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  iam_apikey='1_qpmrC8FREYYCWwFn86o4b7QarYcK2WNNpy-4jXyJMX',
  version='2018-09-21')

response = natural_language_understanding.analyze(
  text='A IBM é uma empresa multinacional com escritório na cidade de São Paulo. '
  'Nesta empresa trabalham diversas pessoas. Entre elas, o João da Silva e a Maria do Carmo.',
  language='pt',
  features=Features(
    entities=EntitiesOptions())).get_result()

print(json.dumps(response, indent=2))

response = natural_language_understanding.analyze(
  text='O jogador de futebol Zezé foi o responsável pelo campeonato do Fluminense. Hoje o Rio de Janeiro está em festa!',
  language='pt',
  features=Features(
    entities=EntitiesOptions())).get_result()

print(json.dumps(response, indent=2))