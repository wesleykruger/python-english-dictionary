import requests
import config
import json

print('Enter a word:')
word = input()

request_url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={config.api_key}'

response = requests.get(request_url)

JSONRes = json.loads(response.text)

print(JSONRes[0]['shortdef'][1])