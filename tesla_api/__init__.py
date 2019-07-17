from datetime import datetime, timedelta
import requests
from .vehicle import Vehicle

BASE_URL = 'https://owner-api.teslamotors.com/'
TOKEN_URL = BASE_URL + 'oauth/token'
API_URL = BASE_URL + 'api/1'
TESLA_CLIENT_ID = '81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384'
TESLA_CLIENT_SECRET = 'c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3'

class AuthenticationError(Exception):
    def __init__(self, error):
        super().__init__('Authentication to the Tesla API failed: {}'.format(error))

class ApiError(Exception):
    def __init__(self, error):
        super().__init__('Tesla API call failed: {}'.format(error))

class TeslaApp:
    def __init__(self, email, password):
        self._email = email
        self._password = password
        self._token = None

    def _get_token(self):
        payload = {
            'grant_type': "password",
            'client_id': TESLA_CLIENT_ID,
            'client_secret': TESLA_CLIENT_SECRET,
            'email': self._email,
            'password': self._password
        }

        response = requests.post(TOKEN_URL, data = payload)
        response_json = response.json()

        if 'response' in response_json:
            raise AuthenticationError(response_json["response"])

        return response_json

    def _refresh_token(self, refresh_token):
        payload = {
            'grant_type': "refresh_token",
            'client_id': TESLA_CLIENT_ID,
            'client_secret': TESLA_CLIENT_SECRET,
            'refresh_token': refresh_token
        }

        response = requests.post(TOKEN_URL, data = payload)
        response_json = response.json()

        if 'response' in response_json:
            raise AuthenticationError(response_json["response"])

        return response_json

    def authenticate(self):
        if self._token is None:
            self._token = self._get_token()
        expire_time = timedelta(seconds=self._token['expires_in'])
        expire_date = datetime.fromtimestamp(self._token['created_at']) + expire_time

        if datetime.now() >= expire_date:
            self._token = self._refresh_token(self._token['refresh_token'])

    def _get_headers(self):
        return {
            'Authorization': 'Bearer {}'.format(self._token['access_token'])
        }

    def post(self, endpoint, data = {}):
        self.authenticate()

        response = requests.post('{}/{}'.format(API_URL, endpoint), headers=self._get_headers(), data=data)
        response_json = response.json()

        if 'error' in response_json:
            raise ApiError(response_json['error'])

        return response_json['response']

    def get_vehicles(self):
        self.authenticate()
        response = requests.get((API_URL + '/vehicles'), headers = self._get_headers())
        response_json = response.json()

        if 'error' in response_json:
            raise ApiError(response_json['error'])

        return [Vehicle(self, vehicle) for vehicle in response_json['response']]
