# encoding=utf8
import redis
from flask import Flask,render_template, request
from flask_socketio import SocketIO, emit
# from flask_sockets import Sockets
import pickle,json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO()
socketio.init_app(app)


members = dict()
name_space = "/upload"


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/admin")
def admin():
    return render_template('admin.html')


@app.route("/api/load", methods=["GET", "POST"])
def show():
    data = str(json.loads(r.get("gridKey")))
    return data


@socketio.on('update', namespace=name_space)
def test_message(message):
    for i in message:
        key = i
        value = message[i]
    print(key)
    value = json.dumps(value)
    r.set(key,value)


@app.route("/api/upload", methods=["POST"])
def ajax():
    data = request.get_data()
    # data = json.loads(data)
    print(data)
    print(type(data))
    # r.set("Nov", data)
    return "success"


if __name__ == "__main__":
    r = redis.Redis(host='127.0.0.1', port=6379, password='passwd', decode_responses=True)
    # app.run(debug=True)
    socketio.run(app, host="127.0.0.1" )
