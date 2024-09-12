class Book:
    id:int
    title:str
    author:str
    published_date:str
    isbn:str
    page_count:int

    def __init__(self, id:int, title:str, author:str, published_date:str, isbn:str, page_count:int):
        self.id = id
        self.title = title
        self.author = author
        self.published_date = published_date
        self.isbn = isbn
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "published_date": self.published_date,
            "isbn": self.isbn,
            "page_count": self.page_count
        }
    
