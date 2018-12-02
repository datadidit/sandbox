"""
    Utility methods for authenticating
"""
import json
import requests
import re
import urllib
import urlparse

import jwt
from jwt.algorithms import RSAAlgorithm
from jose import jwt as jose_jwt
from jose import jws as jose_jws
from python.okta import IDENTITY_PROVIDER, CLIENT_ID

AUTHENTICATION_URL = IDENTITY_PROVIDER + '/api/v1/authn'
AUTHORIZATION_URL = IDENTITY_PROVIDER + '/v1/authorize'
# https://developer.okta.com/docs/api/resources/oidc#1-single-sign-on-to-okta
KEYS_URL = IDENTITY_PROVIDER+'/oauth2/v1/keys'
not_alpha_numeric = re.compile('[^a-zA-Z0-9]+')
public_keys = {}
allowed_domains = ['okta.com', 'oktapreview.com']


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
    print "My Keys URL {0}".format(KEYS_URL)
    response = requests.get(KEYS_URL)

    return json.loads(response.text)['keys']


def create_authorize_url(**kwargs):
    # Taken from
    base_url = kwargs['base_url']
    del(kwargs['base_url'])
    redirect_url = "{}/oauth2/v1/authorize?{}".format(
        base_url,
        urllib.urlencode(kwargs),
    )
    return redirect_url


def okta_pyjwt_decode(id_token):
    keys = get_public_keys()

    for key in keys:
        alg = key['alg']
        kid = key['kid']
        public_key = RSAAlgorithm.from_jwk(json.dumps(key))
        print dir(public_key)
        print public_key.verifier
        try:
            decode = jwt.decode(id_token, public_key, algorithms='RS256', audience=CLIENT_ID, headers={
                'kid': kid
            })
            return decode
        except Exception as e:
            print e


def domain_name_for(url):
    second_to_last_element = -2
    domain_parts = url.netloc.split('.')
    (sld, tld) = domain_parts[second_to_last_element:]
    return sld + '.' + tld


def fetch_jwt_public_key_for(id_token=None):
    if id_token is None:
        raise NameError('id_token is required')

    dirty_header = jose_jws.get_unverified_header(id_token)
    cleaned_key_id = None
    if 'kid' in dirty_header:
        dirty_key_id = dirty_header['kid']
        cleaned_key_id = re.sub(not_alpha_numeric, '', dirty_key_id)
    else:
        raise ValueError('The id_token header must contain a "kid"')
    if cleaned_key_id in public_keys:
        return public_keys[cleaned_key_id]

    unverified_claims = jose_jwt.get_unverified_claims(id_token)
    dirty_url = urlparse.urlparse(unverified_claims['iss'])
    if domain_name_for(dirty_url) not in allowed_domains:
        raise ValueError('The domain in the issuer claim is not allowed')
    cleaned_issuer = dirty_url.geturl()
    oidc_discovery_url = "{}/.well-known/openid-configuration".format(
        cleaned_issuer)
    r = requests.get(oidc_discovery_url)
    openid_configuration = r.json()
    print "OIDC discovery url {0}".format(oidc_discovery_url)
    jwks_uri = openid_configuration['jwks_uri']
    print jwks_uri
    r = requests.get(jwks_uri)
    jwks = r.json()
    for key in jwks['keys']:
        jwk_id = key['kid']
        public_keys[jwk_id] = key

    print cleaned_key_id
    print public_keys.viewkeys()
    print cleaned_key_id in public_keys
    print dirty_key_id in public_keys
    if cleaned_key_id in public_keys:
        return public_keys[cleaned_key_id]
    elif dirty_key_id in public_keys:
        return public_keys[dirty_key_id]
    else:
        raise RuntimeError("Unable to fetch public key from jwks_uri")


def parse_jwt(id_token):
    public_key = fetch_jwt_public_key_for(id_token)
    rv = jose_jwt.decode(
        id_token,
        public_key,
        algorithms='RS256',
        issuer=IDENTITY_PROVIDER,
        audience=CLIENT_ID)
    return rv


def okta_pyjose_decode(id_token):
    key = fetch_jwt_public_key_for(id_token)
    alg = key['alg']

    try:
        decode = jose_jwt.decode(
            id_token,
            key,
            algorithms=alg,
            issuer=IDENTITY_PROVIDER,
            audience=CLIENT_ID
        )
        print decode
    except Exception as e:
        print e
