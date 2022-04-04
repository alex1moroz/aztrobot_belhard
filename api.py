import requests


def aztro(sign, day):
    url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
    query = {"sign": sign, "day":day}
    headers = {"X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com",
               "X-RapidAPI-Key": "88eb68d71emsh155a890ddcc284fp138c10jsn1283285b7382"
               }
    resp = requests.post(url, headers=headers, params=query)
    return resp.json()['description']