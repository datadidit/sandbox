from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def socket():
    return render_template("index.html")


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name="World"):
    return "Hello %s" % name


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)


if __name__ == "__main__":
    socketio.run(app)
