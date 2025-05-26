# from flask import Flask, request, jsonify
# from pymongo import MongoClient
# import datetime

# app = Flask(__name__)

# # MongoDB Connection - Replace with your Atlas URI
# client = MongoClient("mongodb+srv://lakshyapaliwal2003:hi3H190qZ719BAID@cluster0.vwup34a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# db = client.todoapp
# todos = db.todos

# @app.route('/submittodoitem', methods=['POST'])
# def submit_todo():
#     # Manual CORS headers
#     if request.method == 'OPTIONS':
#         return _build_cors_preflight_response()
#     elif request.method == 'POST':
#         return _process_todo_submission()

# def _build_cors_preflight_response():
#     response = jsonify({"message": "Preflight OK"})
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     response.headers.add("Access-Control-Allow-Headers", "*")
#     response.headers.add("Access-Control-Allow-Methods", "*")
#     return response

# def _process_todo_submission():
#     try:
#         data = request.get_json()
#         if not data or 'itemName' not in data:
#             return jsonify({"error": "Item name required"}), 400
        
#         result = todos.insert_one({
#             "itemName": data['itemName'],
#             "itemDescription": data.get('itemDescription', ''),
#             "createdAt": datetime.datetime.utcnow()
#         })
        
#         response = jsonify({
#             "message": "Todo saved",
#             "id": str(result.inserted_id)
#         })
#         response.headers.add("Access-Control-Allow-Origin", "*")
#         return response, 201
        
#     except Exception as e:
#         response = jsonify({"error": str(e)})
#         response.headers.add("Access-Control-Allow-Origin", "*")
#         return response, 500

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from pymongo import MongoClient
import datetime

app = Flask(__name__)

# Enable CORS for all routes
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
    return response

@app.route('/submittodoitem', methods=['POST', 'OPTIONS'])
def submit_todo():
    if request.method == 'OPTIONS':
        # Handle preflight request
        return jsonify({'status': 'preflight'}), 200
    
    try:
        data = request.get_json()
        
        # MongoDB operations
        result = todos.insert_one({
            "itemName": data['itemName'],
            "itemDescription": data.get('itemDescription', ''),
            "createdAt": datetime.datetime.utcnow()
        })
        
        return jsonify({
            "message": "Todo saved successfully",
            "id": str(result.inserted_id)
        }), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)