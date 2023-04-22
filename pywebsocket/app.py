from gevent import monkey
monkey.patch_all()

import cgi
import redis
from flask import Flask, render_template, request, url_for
from flask_socketio import SocketIO

count = 0
app = Flask(__name__)


# db = redis.StrictRedis('localhost', 6379, 0)

def get_status(is_incr=False):
    with open("./counter.txt") as fh:
        try:
            count = int(fh.read())
        except ValueError:
            count = 0

        if is_incr == True:
            count += 1
        else:
            count -= 1

    with open("./counter.txt", "w") as fh:
        fh.write(str(count))
        return count

socketio = SocketIO(app)


@app.route('/')
def main():
    jquery_url = url_for("static", filename="jquery-1.11.1.min.js")
    sock_url = url_for("static", filename="socket.io.min-1.4.5.js")

    # print(jquery_url, sock_url)
    return render_template('main.html', jquery_url=jquery_url, sock_url=sock_url)


@app.route('/pymeetups/')
def pymeetups():
    return render_template('pymeetups.html')


@socketio.on('connect', namespace='/dd')
def ws_conn():
    c = get_status(True)  #db.incr('connected')
    print(f"COunt: {c}")
    socketio.emit('msg', {'count': c}, namespace='/dd')


@socketio.on('disconnect', namespace='/dd')
def ws_disconn():
    c = get_status(False) #db.decr('connected')
    print(f"COunt: {c}")
    socketio.emit('msg', {'count': c}, namespace='/dd')

@socketio.on('city', namespace='/dd')
def ws_city(message):
    print(message['city'])
    socketio.emit('city', {'city': cgi.escape(message['city'])},
                  namespace="/dd")

import random
import time
@app.route("/update", methods=["GET"])
def update_status():
    # while True:
    #     n = random.randint(1, 5)
    #     for i in range(n):
    #         print(f"Will update in {n-i} seconds...", end="\r")
    #         time.sleep(1)
    c = get_status(is_incr=True)
    socketio.emit('msg', {'count': c}, namespace='/dd')
    return {"count": c}

if __name__ == '__main__':
    print("Running on... <http://127.0.0.1:5000/>")
    socketio.run(app, "0.0.0.0", port=5000)#, async_mode='threading')

    # import threading
    # t = threading.Thread(target=update_status)
    # t.start()

    # To keep updating call this API
    # http://127.0.0.1:5000/update



