from flask import Blueprint, request, url_for, redirect
from python.okta import IDENTITY_PROVIDER, CLIENT_ID
from python.okta.utils.authenticate import login, create_authorize_url
from pprint import pprint

authenticate = Blueprint("authenticate", __name__)


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
        scope='openid',
        response_type='id_token',
        response_mode='form_post',
        nonce='FakeNonce',
        state='FakeState',
        redirect_uri=redirect_uri
        )

    return redirect(redirect_url)


@authenticate.route("/sso/oidc", methods=["GET", "POST"])
def sso_oidc():
    print request
    print request.path
    print request.values
    print dir(request)
    t = pprint(request)
    print t
    # id_token = request.form['id_token']
    print "DID I GET HERE!!!!"
    # print id_token
    # return id_token
    return "ok"


@authenticate.route("/jello")
def jello():
    return "jello"