from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.event
def my_event(message):
    emit('my_response', {'data': message['data']})

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=8080)