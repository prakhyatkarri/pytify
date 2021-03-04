import json

from api.request import token


def get_secrets():
    """ Get Config Secrets File data"""
    try:
        with open('config/secrets.json') as secret_file:
            return json.load(secret_file)
    except Exception as e:
        print(f'Exception in main: {e}')


if __name__ == '__main__':
    config_secrets = get_secrets()

    client_id = config_secrets['clientId']
    secret = config_secrets['secret']

    token = token.get_token(client_id, secret)
    print(token)
