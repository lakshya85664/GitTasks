from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from werkzeug.exceptions import InternalServerError

app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://lakshyapaliwal2003:hi3H190qZ719BAID@cluster0.vwup34a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["form"]
collection = db["submissions"]

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        data = {
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "message": request.form.get('message')
        }
        
        # Insert into MongoDB
        result = collection.insert_one(data)
        
        # Redirect on success
        return redirect(url_for('success'))
        
    except Exception as e:
        # Return error message on failure
        return render_template('form.html', error=str(e)), 500

@app.route('/success')
def success():
    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)