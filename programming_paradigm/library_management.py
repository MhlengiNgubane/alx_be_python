class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = checked_out
        
class Library:
    def __init__(self):
        self._book = []
        
    def add_book(self, title, author):
        """Add a new Book to the library."""
        new_book = Book(title, author)
        self._books.append(new_book)
    
    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False
    
    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  
    
    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book.title for book in self._books if not book._is_checked_out]
        if available_books:
            return available_books
        else:
            return "No available books."  