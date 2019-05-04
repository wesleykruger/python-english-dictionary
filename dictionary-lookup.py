import requests
import config
import json
import test.test_json

print('Enter a word:')
word = input()
print(word)


request_url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={config.api_key}'


response = requests.get(request_url)

print(response.content[0].meta.id)
