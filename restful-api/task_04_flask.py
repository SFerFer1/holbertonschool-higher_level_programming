from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
userss =[]
users = {"jane": {"username": "jane", "name": "jane", "age": 28, "city": "Los Angeles"}, 
"john": {"username": "john", "name": "john", "age": 30, "city": "New York"}}

for user in users:
    userss.append(user)
@app.route('/')
def home():
     return "“Welcome to the Flask API!”"

@app.route('/data')
def data():
    return jsonify(userss)
    
@app.route('/status')
def status():
     return "OK"

@app.route('/users/<username>')
def users(username):
    for user in users:
        if (user == username):
            return jsonify(user)
    return {"error": "User not found"}

@app.route('/add_user')
def add_user(add_user):
    return add_user
if __name__ == "__main__":
    app.run()

