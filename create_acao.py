from random import randint

import requests
from get_url import url

url += "/acoes"


def create_acao(acao_data, headers):
    response = requests.post(url=url, json=acao_data, headers=headers)

    if response.status_code == 201:
        id = response.headers['Location'][len(url) + 1:]
        print("Ação " + id + " Created")
        return id
    else:
        print("ERROR " + str(response.status_code) + ": ")
        print(response.text)
        exit()
