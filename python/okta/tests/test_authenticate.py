"""
    Test authentication
"""
import json
import os
import pytest
import requests
import responses
from python.okta.utils.authenticate import get_public_keys, login, KEYS_URL, AUTHENTICATION_URL, okta_pyjwt_decode, \
    okta_pyjose_decode, parse_jwt, fetch_jwt_public_key_for

FILE_PATH = os.path.dirname(__file__)


def _get_key_response():
    return open(FILE_PATH + '/data/keys_response.json').read()


def _get_login_response():
    return open(FILE_PATH + "/data/login_response.json").read()


def _get_id_token():
    return open(FILE_PATH + "/data/latest_id_token").read()


@responses.activate
def test_authenticate_flow():
    responses.add(responses.GET, KEYS_URL, json=_get_key_response(), status=200)

    keys = get_public_keys()
    assert keys == json.loads(_get_key_response())


@responses.activate
def test_login():
    responses.add(responses.POST, AUTHENTICATION_URL, json=_get_login_response(), status=200)

    result = login("test@gmail.com", "sNh5kNm9")

    assert result == json.loads(_get_login_response())


def test_verify():
    token = okta_pyjwt_decode(_get_id_token())
    print token
    """
    print "use python_jose instead"
    token = okta_pyjose_decode(_get_id_token())

    print "use copied jose"
    token = parse_jwt(_get_id_token())
    print token
    """

def test_key_diff():
    ''' What is diff '''
    my_keys = get_public_keys()

    copied_key = fetch_jwt_public_key_for(_get_id_token())

    print my_keys
    print "==============================="
    print copied_key


@pytest.mark.skip
def test_login():
    # Gives you the `id_token`
    response = requests.get("http://localhost:8080/login?username=mkwyche@gmail.com&password=Altheia1208")

    print response.status_code
    print "===================="
    print response.text

    print "============= JSON =============="
    print response.json