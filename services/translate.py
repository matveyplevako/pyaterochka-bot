import requests
from os import environ


def translate(my_text, from_lang="en", to="ru"):
    params = {
        "key": environ["TRANSLATE_KEY"],
        "text": my_text,
        "lang": 'en-ru'
    }
    response = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate", params=params)
    return response.json()['text'][0]
