class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author))

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.title < other.title
        return NotImplemented

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return f"Library with {len(self)} books"

# Create books
book1 = Book("1984", "George Orwell")
book2 = Book("Brave New World", "Aldous Huxley")
book3 = Book("Animal Farm", "George Orwell")

# Create library and add books
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Test __len__ by printing length of library
print(f"The library has {len(library)} books.")

# Display library's string representation
print(library)
