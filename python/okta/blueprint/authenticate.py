from flask import Blueprint, request, url_for, redirect, jsonify, Response
from python.okta import IDENTITY_PROVIDER, CLIENT_ID
from python.okta.utils.authenticate import login, create_authorize_url, okta_pyjose_decode, okta_pyjwt_decode, \
    fetch_jwt_public_key_for, parse_jwt

authenticate = Blueprint("authenticate", __name__)


@authenticate.route("/basic_login")
def basic_login():
    ''' Example of basic authentication'''
    if request.authorization:
        # Once you login once browser will save your credentials
        redirect_uri = url_for("{0}.{1}".format("authenticate", fetch_login.__name__))
        response = redirect(redirect_uri)
        response.headers = {"authorization": request.authorization}
        return response

    return Response("Login is required!", 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})\


@authenticate.route("/login", methods=["GET", "POST"])
def fetch_login():
    '''
    REST endpoint for okta login
    '''
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
    else:
        if request.authorization:
            username = request.authorization.username
            password = request.authorization.password
        else:
            username = request.values.get("username")
            password = request.values.get("password")

    result = login(username, password)

    # If user login is successful dispatch redirection to get an auth token
    redirect_uri = url_for("{0}.{1}".format("authenticate", sso_oidc.__name__),
            _external=True,
            _scheme="http")
    redirect_url = create_authorize_url(
        base_url=IDENTITY_PROVIDER,
        sessionToken=result['sessionToken'],
        client_id=CLIENT_ID,
        scope='openid profile email',
        #response_type='token',
        response_type="id_token",
        response_mode='form_post',
        nonce='FakeNonce',
        state='FakeState',
        redirect_uri=redirect_uri
        )

    return redirect(redirect_url)


@authenticate.route("/sso/oidc", methods=["GET", "POST"])
def sso_oidc():
    try:
        # Id token flow
        id_token = request.form['id_token']
        decode = okta_pyjwt_decode(id_token)
        # Goes with token response_type
        # access_token = request.form['access_token']
        # decode = okta_pyjwt_decode(access_token)
        return jsonify(decode)
    except Exception as e:
        print request.form
        raise e


@authenticate.route("/jello")
def jello():
    return "jello"