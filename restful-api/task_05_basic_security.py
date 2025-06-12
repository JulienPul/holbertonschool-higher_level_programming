#!/usr/bin/python3
"""API Security and Authentication Techniques"""
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {"alice": generate_password_hash("alice123"),
    "bob": generate_password_hash("bob456")}

@auth.verify_password
def verify_password(username, password):
    """verify password"""
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
    return None

@app.route("/basic-protected")
@auth.login_required
def basic_auth():
    """basic authentification"""
    return jsonify({"Basic Auth: Access Granted"})

if __name__ == '__main__':
    app.run()
