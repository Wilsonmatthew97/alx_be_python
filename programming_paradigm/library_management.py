class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False
    
    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self.__is_checked_out

class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Only book instances can be added.")
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"You checked out: {book.title}")
                return
        print(f"{title} is not available.")
     
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"You returned: {book.title}")
        print(f"{title} was not checked out.")
    
    def list_available_books(self):
        available = [book for book in self.__books if book.is_available()]
        if not available:
            print("No book currently available.")
        else:
            for book in available:
                print(f"- {book.title} by {book.author}")
