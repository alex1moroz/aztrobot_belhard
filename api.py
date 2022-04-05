import requests
from decouple import config

token = config('AZTRO_TOKEN',default='')


def aztro(sign, day):
    url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
    query = {"sign": sign, "day":day}
    headers = {"X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com",
               "X-RapidAPI-Key": token
               }
    resp = requests.post(url, headers=headers, params=query)
    return resp.json()['description']