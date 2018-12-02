"""
    Utility methods for authenticating
"""
import urllib
import json
import requests
from python.okta import IDENTITY_PROVIDER, CLIENT_ID

AUTHENTICATION_URL = IDENTITY_PROVIDER + '/api/v1/authn'
AUTHORIZATION_URL = IDENTITY_PROVIDER + '/v1/authorize'
KEYS_URL = IDENTITY_PROVIDER+'/oauth2/default/v1/keys'


def login(username, password):
    '''
        Login a user
    :param username:
    :param password:
    :return:
    '''
    data = {
        "username": username,
        "password": password
    }

    response = requests.post(AUTHENTICATION_URL, json=data)
    return json.loads(response.text)


def get_public_keys():
    '''
        Get public keys from okta
    :return:
    '''
    response = requests.get(KEYS_URL)

    return json.loads(response.text)


def create_authorize_url(**kwargs):
    # Taken from
    base_url = kwargs['base_url']
    del(kwargs['base_url'])
    redirect_url = "{}/oauth2/v1/authorize?{}".format(
        base_url,
        urllib.urlencode(kwargs),
    )
    return redirect_url
