from flask import Flask, render_template, url_for
from python.okta.blueprint import authenticate
from python.okta.utils.authenticate import create_authorize_url
from python.okta import CLIENT_ID, IDENTITY_PROVIDER
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(authenticate)


# Actual SPA
@app.route("/axios_cors_bs")
def login_user():
    target_origin = url_for('login_user', _external=True, _scheme='http')
    return render_template("login.html",
                           target_origin=target_origin)

@app.route("/")
def basic_login():
    target_origin = url_for('basic_login', _external=True, _scheme='http')
    return render_template("basic.html",
                           target_origin=target_origin)

@app.route("/correct")
def main_page():
    """

    if len(required.keys()) > 0:
        return render_template(
            'error.html',
            required=required,
            okta=okta)
    """

    redirect_uri = url_for(
        'authenticate.sso_oidc',
        _external=True,
        _scheme='http')

    login_with_okta_branding = create_authorize_url(
        base_url=IDENTITY_PROVIDER,
        client_id=CLIENT_ID,
        scope='openid',
        response_type='id_token',
        response_mode='form_post',
        nonce='FakeNonce',
        state='FakeState',
        redirect_uri=redirect_uri)
    target_origin = url_for('main_page', _external=True, _scheme='http')
    return render_template(
        'main_page.html',
        target_origin=target_origin,
        login_with_okta_branding=login_with_okta_branding,
        okta={
            "smdf": 1
        })


# app.register_blueprint(authenticate)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)