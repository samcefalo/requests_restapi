import requests
from get_url import url

url += "/jogos"


def create_jogo(jogo_data, headers):
    response = requests.post(url=url, json=jogo_data, headers=headers)

    if response.status_code == 201:
        id = response.headers['Location'][len(url) + 1:]
        print("Jogo " + id + " Created")
        return id
    else:
        print("ERROR " + str(response.status_code) + ": ")
        print(response.text)
