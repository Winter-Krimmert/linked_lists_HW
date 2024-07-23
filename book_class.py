class Book:
    def __init__(self, title, author, genre, isbn, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.quantity = quantity

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, ISBN: {self.isbn}, Quantity: {self.quantity}"
