import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, MetadataOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  iam_apikey='{iam_api_key}',
  version='2018-09-21')

response = natural_language_understanding.analyze(
  url='www.folha.com.br',
  language='pt',
  features=Features(
    metadata=MetadataOptions())).get_result()

print(json.dumps(response, indent=2))

response = natural_language_understanding.analyze(
  url='http://www.serpro.gov.br/',
  language='pt',
  features=Features(
    metadata=MetadataOptions())).get_result()

print(json.dumps(response, indent=2))