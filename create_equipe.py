import requests
from get_url import url
from utils import get_random_string

url += "/equipes"

equipe_data = {
    "nome": get_random_string(10),
}


def create_equipe(headers):
    response = requests.post(url=url, json=equipe_data, headers=headers)

    if response.status_code == 201:
        id = response.headers['Location'][len(url) + 1:]
        print("Equipe " + id + " Created")
        return id
    else:
        print("ERROR " + str(response.status_code) + ": ")
        print(response.text)
