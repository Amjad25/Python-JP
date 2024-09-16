from flask import Flask, jsonify, request

from controller.books import *

app:Flask = Flask(__name__)

app.add_url_rule("/books", view_func=allBooks, methods=["GET"])
app.add_url_rule("/books/<int:id>", view_func=getBook, methods=["GET"])
app.add_url_rule("/books", view_func=addBook, methods=["POST"])
app.add_url_rule("/books/<int:id>", view_func=updateBook, methods=["PUT"])
app.add_url_rule("/books/<int:id>", view_func=deleteBook, methods=["DELETE"])

app.run(
    debug=True, 
    host="localhost",
    port=3000
)

