import db
from flask import Flask, jsonify, request ,make_response
from flask_bcrypt import Bcrypt

db_conn = db.mysqlconnect()

def register():
    cur = db_conn.cursor()
    data = request.json
    print(data)
    user_name = data.get("username")
    password = data.get("password")
    email = data.get("email")
    full_name = data.get("fullname")
    hashed_password = password
    try:
        cur.execute(f"INSERT INTO users (username, password, email, fullname) VALUES ('{user_name}', '{hashed_password}', '{email}', '{full_name}')")
        db_conn.commit()
        return jsonify({"message": "user registered"})
        
    except Exception as e:
        return jsonify({"message": f"error occured :{e}"})


