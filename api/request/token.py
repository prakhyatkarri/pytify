import requests

from api.request.url import URL


def get_token(client_id, secret):
    data = {URL.GRANT_TYPE: URL.CLIENT_CREDENTIALS, URL.CLIENT_ID: client_id, URL.CLIENT_SECRET: secret}
    try:
        response = requests.post(URL.AUTH_URL, data)

        if response and response.status_code == 200:
            return response.json()['access_token']
    except Exception as e:
        print(f'Exception in get_token: {e}')
    return {}
