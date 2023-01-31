from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def test_get():
    return jsonify({'test': 'test response'})

app.run()