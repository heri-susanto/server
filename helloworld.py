from flask import Flask, request
from flask import jsonify
import json
import rekomendasi as rekomendasi
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def hello_world():
    # x = {
    #     "name": "John",
    #     "age": 30,
    #     "city": "New York"
    # }
    # y = json.dumps(x)
    body = request.data
    # y = rekomendasi.recommender('heriganteng')
    
    return body
