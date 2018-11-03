import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  iam_apikey='{iam_api_key}',
  version='2018-09-21')

response = natural_language_understanding.analyze(
  text='Não gostei nenhum pouco do filme.',
  language='pt',
  features=Features(
    sentiment=SentimentOptions())).get_result()

print(json.dumps(response, indent=2))

response = natural_language_understanding.analyze(
  text='Aquela padaria é muito boa!',
  language='pt',
  features=Features(
    sentiment=SentimentOptions())).get_result()

print(json.dumps(response, indent=2))

response = natural_language_understanding.analyze(
  text='Para mim, a qualidade do serviço deles é ok.',
  language='pt',
  features=Features(
    sentiment=SentimentOptions())).get_result()

print(json.dumps(response, indent=2))

