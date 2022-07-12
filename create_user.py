import requests
from get_url import url

url += "/users"


def create_user(user_data):
    response = requests.post(url=url, json=user_data)

    if response.status_code == 201:
        id = response.headers['Location'][len(url) + 1:]
        print("User " + id + " Created")
    else:
        print("ERROR " + str(response.status_code) + ": ")
        print(response.text)
