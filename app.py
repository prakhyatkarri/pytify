import json

from api.request import token

if __name__ == '__main__':
    secrets_path = './config/secrets.json'
    try:
        with open(secrets_path) as secret_file:
            config_secrets = json.load(secret_file)
    except Exception as e:
        print(f'Exception in main: {e}')

    client_id = config_secrets['clientId']
    secret = config_secrets['secret']

    token = token.get_token(client_id, secret)
    print(token)
