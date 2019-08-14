from flask import Flask
from flask import jsonify
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    y = json.dumps(x)
    return jsonify(y)
