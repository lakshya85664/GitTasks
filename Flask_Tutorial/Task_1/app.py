# from flask import Flask

# app = Flask(__name__)

# @app.route('/')

# def home():
#     return "Hello guys"

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

# Configuration
DATA_FILE = 'data.json'
DEFAULT_DATA = [
    {"id": 1, "name": "Example 1"},
    {"id": 2, "name": "Example 2"},
    {"id": 3, "name": "Example 3"}
]

def initialize_data():
    """Create data file if it doesn't exist"""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump(DEFAULT_DATA, f)

@app.route('/api', methods=['GET'])
def api_endpoint():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        initialize_data()
        return jsonify(DEFAULT_DATA)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    initialize_data()
    app.run(host='0.0.0.0', port=5000, debug=True)