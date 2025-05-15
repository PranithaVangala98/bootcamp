class Library:
    total_books = 0  # Class variable to keep track of the total number of books

    def __init__(self, name, books=None):
        self.name = name  # Instance variable to store the library's name
        self.books = books or []  # Instance variable for the list of books in the library
        Library.total_books += len(self.books)  # Update total books when a library is created

    @staticmethod
    def is_valid_isbn(isbn):
        """Static method to check if an ISBN is valid (a simple check)."""
        return len(isbn) == 13 and isbn.isdigit()

    @classmethod
    def from_book_list(cls, name, book_list):
        """Class method to create a Library instance from a list of books."""
        return cls(name, book_list)

    def add_book(self, book):
        """Instance method to add a book to this library's collection."""
        self.books.append(book)
        Library.total_books += 1  # Update the class-level total when a book is added

    def remove_book(self, book):
        """Instance method to remove a book from this library's collection."""
        self.books.remove(book)
        Library.total_books -= 1  # Update the class-level total when a book is removed

    def list_books(self):
        """Instance method to list all the books in this library."""
        return [book.title for book in self.books]

# Book class for demonstration
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

# Creating books
book1 = Book("1984", "George Orwell", "1234567890123")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "1234567890124")
book3 = Book("Brave New World", "Aldous Huxley", "1234567890125")

# Using the class method to create a Library instance
library = Library.from_book_list("City Library", [book1, book2])

# Using the instance method to add a new book
library.add_book(book3)

# Listing books using the instance method
print(f"Books in {library.name}: {library.list_books()}")

# Using the static method to check the validity of an ISBN
isbn_check = Library.is_valid_isbn("1234567890123")
print(f"Is ISBN valid? {isbn_check}")

# Accessing the total books count via the class-level variable
print(f"Total books in all libraries: {Library.total_books}")
