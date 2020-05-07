import json
from threading import Thread
from flask import Flask, request


app = Flask(__name__)
host = '127.0.0.1'
port = 5555

total_data = {}
post_data = {}

# ------------------------------------------------------------------------------------------------------------------
def run_mock():
    server = Thread(target=app.run, kwargs={'host': host, 'port': port})
    server.start()
    return server


# ------------------------------------------------------------------------------------------------------------------
@app.route('/shutdown')
def shutdown():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    terminate_func()


# ------------------------------------------------------------------------------------------------------------------
@app.route('/example/<number>')
def get_some_data(number):
    return f"example #{number}"


# ------------------------------------------------------------------------------------------------------------------
@app.route('/get_data')
def get_data():
    return json.dumps(total_data)


# ------------------------------------------------------------------------------------------------------------------
@app.route('/post_data', methods=["POST"])
def post_data():
    new_data = request.get_json()
    total_data.update(new_data)
    return json.dumps(total_data)


if __name__ == '__main__':
    run_mock()
