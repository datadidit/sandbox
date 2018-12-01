from flask import Flask
from python.okta.blueprint import authenticate

app = Flask(__name__)

app.register_blueprint(authenticate)


# app.register_blueprint(authenticate)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)