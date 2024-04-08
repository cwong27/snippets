import json
from flask import Flask, request, jsonify

app = Flask(__name__)
name = "candidate"
users = dict({"admin":"admin@sample.com"})

@app.route('/', methods=['GET'])
def index():
    return 'Hello {}'.format(name), 200

@app.route('/set_name', methods=['POST'])
def set_name():
    global name
    try: 
        payload = request.get_json()
        new_name = payload["name"]
        message = {
            "message": "Name changed!",
            "old_name": name,
            "new_name": new_name,
        }
        name = new_name
        return message, 201
    except Exception as e:
        return {"error": str(e)}, 500
    
@app.route('/user/<username>', methods=['GET', 'DELETE'])
def get_user(username):
    global users
    try:
        if username not in users.keys():
            return {"message": f"{username} not found."}
        if request.method == 'GET':
            message = {
                "user_name": username,
                "email": users[username],
            }
            return message
        if request.method == 'DELETE':
            del users[username]
            return {"message": f"{username} deleted."}
    except Exception as e:
        return {"error": str(e)}, 500
    
@app.route('/user', methods=['POST'])
def post_user():
    global users
    try:
        payload = request.get_json()
        name = payload["name"]
        email = payload["email"]
        if name in users.keys():
            return {"message": f"{name} already exists."}
        
        users[name] = email
        message = {
            "user_name": name,
            "email": users[name],
        }
        return message
    except Exception as e:
        return {"error": str(e)}, 500
    
@app.route('/user', methods=['PUT'])
def put_user():
    global users
    try:
        payload = request.get_json()
        name = payload["name"]
        email = payload["email"]
        if name not in users.keys():
            return {"message": f"{name} not found."}
        users[name] = email
        message = {
            "user_name": name,
            "email": users[name],
        }
        return message
    except Exception as e:
        return {"error": str(e)}, 500