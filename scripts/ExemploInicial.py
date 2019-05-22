#
# Exemplo inicial de NLU
#

#
# SDK:
# https://github.com/watson-developer-cloud/python-sdk
# 
# pip install --upgrade watson-developer-cloud
#

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  iam_apikey='{iam_api_key}',
  version='2018-09-21')

response = natural_language_understanding.analyze(
  text='A IBM é uma empresa multinacional com escritório na cidade de São Paulo. '
  'Nesta empresa trabalham diversas pessoas. Entre elas, o João da Silva e a Maria do Carmo.',
  language='pt',
  features=Features(
    entities=EntitiesOptions(),
    keywords=KeywordsOptions())).get_result()

print(json.dumps(response, indent=2))