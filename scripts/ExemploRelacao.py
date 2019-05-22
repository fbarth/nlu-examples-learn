import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, RelationsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  iam_apikey='{iam_api_key}',
  version='2018-09-21')

response = natural_language_understanding.analyze(
  text='The Nobel Prize in Physics 1921 was awarded to Albert Einstein',
  language='en',
  features=Features(
    entities=EntitiesOptions(),
    relations=RelationsOptions())).get_result()

print(json.dumps(response, indent=2))