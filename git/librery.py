from book import Book

class Library:
    def __init__(self):
        self.books = []
        self.borrow_book = []

    def add_book(self, book):
         self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return "Book not found"
    
    def borrow_book(self, title):
        book = self.find_book(title)
        if isinstance(book, Book):
            self.borrow_book.append(book)
            self.books.remove(book)
            return f"You have borrowed '{book.title}'"
        return book
    
    def return_book(self, title):
        for book in self.borrow_book:
            if book.title == title:
                self.books.append(book)
                self.borrow_book.remove(book)
                return f"You have returned '{book.title}'"
        return "This book was not borrowed"
        