from flask import Flask, jsonify, request
from methods import register
# from flask_bcrypt import Bcrypt


app:Flask = Flask(__name__)
# bcrypt = Bcrypt(app)

app.add_url_rule("/register", view_func=lambda: register, methods=["POST"])


app.run(
    debug=True, 
    host="localhost",
    port=3000
)

