from book import Book

from flask import Flask, jsonify, request

app:Flask = Flask(__name__)
books:Book = []

@app.route("/")
def allBooksInitial():
    return books


#  get all books
@app.route("/books", methods=["GET"])
def allBooks():
    # return as json object
    return jsonify([book.to_dict() for book in books])



#  get single book by id
@app.route("/books/<int:id>", methods=["GET"])
def getBook(id):
    for book in books:
        if book.id == id:
            return jsonify(book.to_dict())
    return "Book not found" 



# add book Post API by taking raw data
@app.route("/books", methods=["POST"])
def addBook():
    book = Book(len(books)+1, request.json["title"], request.json["author"], request.json["published_date"], request.json["isbn"], request.json["page_count"])
    books.append(book)
    return "Book added \n" + str(book)


# update book by id
@app.route("/books/<int:id>", methods=["PUT"])
def updateBook(id):
    for book in books:
        if book.id == id:
            book.title = request.json["title"]
            book.author = request.json["author"]
            book.published_date = request.json["published_date"]
            book.isbn = request.json["isbn"]
            book.page_count = request.json["page_count"]
            return "Book updated \n" + str(book)
    return "Book not found"

#  delete book by id
@app.route("/books/<int:id>", methods=["DELETE"])
def deleteBook(id):
    for book in books:
        if book.id == id:
            books.remove(book)
            return "Book deleted"
    return "Book not found"


app.run(
    debug=True, 
    host="localhost",
    port=3000
)


