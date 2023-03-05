import requests
from flask import request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

JSON_SERVER_URL = "http://localhost:3000"


@app.route('/users/signup', methods=['POST'])
def signup():
    data = request.json
    response = requests.post('{}/users'.format(JSON_SERVER_URL), json=data)
    return jsonify(response.json()), response.status_code


@app.route('/users/login', methods=['POST'])
def login():
    data = request.json
    response = requests.get("{}/users?email={data['email']}&password={data['password']}".format(JSON_SERVER_URL))
    if response.ok:
        return jsonify(response.json()), response.status_code
    else:
        return jsonify({'error': 'Invalid credentials'}), 401