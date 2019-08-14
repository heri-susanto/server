from flask import Flask, request
from flask import jsonify
import json
import rekomendasi as rekomendasi
app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    # x = {
    #     "name": "John",
    #     "age": 30,
    #     "city": "New York"
    # }
    # y = json.dumps(x)
    body = request.get_data(as_text=True)
    # y = rekomendasi.recommender('heriganteng')
    return body
