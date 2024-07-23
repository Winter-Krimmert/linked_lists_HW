from book_class import Book
from node_class import Node

class InventoryManager:
    def __init__(self):
        self.head = None

    def add_book(self, title, author, genre, isbn, quantity):
        new_book = Book(title, author, genre, isbn, quantity)
        new_node = Node(new_book)
        new_node.next = self.head
        self.head = new_node

    def remove_book(self, isbn):
        current = self.head
        prev = None
        while current is not None and current.book.isbn != isbn:
            prev = current
            current = current.next
        if current is None:
            return False
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        return True

    def display_inventory(self):
        current = self.head
        while current is not None:
            print(current.book)
            current = current.next
