from random import randint

import requests
from get_url import url

url += "/atletas"


def create_atleta(atleta_data, headers):
    response = requests.post(url=url, json=atleta_data, headers=headers)

    if response.status_code == 201:
        id = response.headers['Location'][len(url) + 1:]
        print("Atleta " + id + " Created")
        return id
    else:
        print("ERROR " + str(response.status_code) + ": ")
        print(response.text)
        exit()
