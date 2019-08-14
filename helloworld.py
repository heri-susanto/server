from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    d = 'Hello, World!'
    return jsonify(d)
