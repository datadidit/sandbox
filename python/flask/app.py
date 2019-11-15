import logging
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

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
    logging.info('received message: ' + message)


@socketio.on('my_echo', namespace='/draft')
def test_message(message):
    logging.info('GOT my_echo: %s' % message)
    emit('my_response',
         {'data': message['data']})


@socketio.on('my_broadcast_event', namespace='/draft')
def test_broadcast_message(message):
    logging.info('GOT my_broadcast')
    emit('my_response',
         {'data': message['data']},
         broadcast=True)


@socketio.on('my_ping', namespace='/draft')
def ping_pong():
    emit('my_pong')


if __name__ == "__main__":
    socketio.run(app)
