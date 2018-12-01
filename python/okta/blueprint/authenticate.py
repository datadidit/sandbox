from flask import Blueprint

authenticate = Blueprint("authenticate", __name__)


@authenticate.route("/")
def hello():
    return "ok"
