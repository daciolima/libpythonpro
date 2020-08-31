import requests


def buscar_avatar(usuario):
    """
    Buscar um avatar de um usuário no github.

    :param usuario: str - Nome do usuário a ser buscado no Avatar do github
    :return: str com o link do do avatar do github
    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('daciolima'))
