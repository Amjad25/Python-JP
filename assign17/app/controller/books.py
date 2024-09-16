#  get all books
from flask import jsonify, request

from assign17.book import Book

# from book import Book
books:Book = [
    Book(1, "Book 1", "Author 1", "2021-01-01", "1234", 100),
    Book(2, "Book 2", "Author 2", "2021-01-01", "1234", 100),
    Book(3, "Book 3", "Author 3", "2021-01-01", "1234", 100),
]


def allBooks():
    # return as json object
    return jsonify([book.to_dict() for book in books])



#  get single book by id
def getBook(id):
    for book in books:
        if book.id == id:
            return jsonify(book.to_dict())
    return "Book not found" 



# add book Post API by taking raw data
def addBook():
    book = Book(len(books)+1, request.json["title"], request.json["author"], request.json["published_date"], request.json["isbn"], request.json["page_count"])
    books.append(book)
    return "Book added \n" + str(book)


# update book by id
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
def deleteBook(id):
    for book in books:
        if book.id == id:
            books.remove(book)
            return "Book deleted"
    return "Book not found"
