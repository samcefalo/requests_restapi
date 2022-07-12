import requests
from get_url import url

url += "/login"


def login(user_data):
    response = requests.post(url=url, json=user_data)

    if response.status_code == 200:
        print("Logged")
        token = response.headers['Authorization']
        return token
    else:
        print("ERROR " + str(response.status_code) + ": ")
        print(response.text)
