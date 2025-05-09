class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author))

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Create books
book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")
book3 = Book("Animal Farm", "George Orwell")

# Use in a set
book_set = {book1, book2, book3}

# Output
for book in book_set:
    print(book)
