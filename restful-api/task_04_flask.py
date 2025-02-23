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
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user(add_user):
    new_user = request.get_json()
    if "username" in new_user and "name" in new_user and "age" in new_user and "city" in new_user:
        users[new_user["username"]] = new_user
        return jsonify({"message": "User added successfully"}), 201
    return jsonify({"error": "Invalid data"}), 400

    return add_user
if __name__ == "__main__":
    app.run()

