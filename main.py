import time
from random import randint
from random import choice

from create_acao import create_acao
from create_atleta import create_atleta
from create_jogo import create_jogo
from utils import get_random_string
from create_user import create_user
from create_equipe import create_equipe
from login import login

nome = get_random_string(10)
email = nome + "@teste.com"
senha = "123456"

option = 0
while option not in [1,2]:
    print("1 - Create new user")
    print("2 - Login with registered user")
    option = int(input('Choice an option: '))

if option == 2:
    email = input('E-mail: ')
    senha = input('Password: ')

user_data = {
    "nome": nome,
    "senha": senha,
    "email": email
}

login_data = {
    "email": email,
    "senha": senha
}

if option == 1:
    create_user(user_data)

token = login(login_data)

headers = {
    'Authorization': token
}

equipes = list()
equipes.append(create_equipe(headers))
equipes.append(create_equipe(headers))

atleta_amount = int(input('Enter the number of athletes: '))
atletas = {}

for i in range(atleta_amount):
    equipe = choice(equipes)
    atleta_data = {
        "nome": get_random_string(7),
        "numero": randint(1, 50),
        "data_nascimento": "2008-05-01",
        "sexo": randint(1, 3),
        "equipe": {
            "id": equipe
        },
    }
    atletas[create_atleta(atleta_data, headers)] = equipe
    time.sleep(0.5)

jogo_data = {
    "esporte": randint(1, 2),
    "tipo": randint(1, 4),
    "equipes": [{
        "id": equipes[0]
    }, {
        "id": equipes[1]
    }]
}

jogo_id = create_jogo(jogo_data, headers)

bool_list = ["true", "false"]
acoes_list = ["Desarme", "Drible", "Finalizacao", "Passe", "Recepcao"]
placar_list = ["0x0", "1x0", "1x1", "2x0", "2x1", "2x2", "0x1", "0x2"]

acao_amount = int(input('Enter the number of actions: '))

for i in range(acao_amount):
    atleta = choice(list(atletas))
    equipe = atletas[atleta]
    acao_data = {
        "@tipo": choice(acoes_list),
        "grauDificuldade": randint(1, 4),
        "area": randint(1, 3),
        "gol": choice(bool_list),
        "placar": choice(placar_list),
        "posseDeBola": choice(bool_list),
        "equipe": {
            "id": equipe
        },
        "atleta": {
            "id": atleta
        },
        "jogo": {
            "id": jogo_id
        },
        "exito": choice(bool_list)
    }
    create_acao(acao_data, headers)
    time.sleep(0.5)

print("-" * 20)
print("Finish")
print("-" * 20)
