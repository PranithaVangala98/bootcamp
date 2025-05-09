class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author))

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.title < other.title
        return NotImplemented

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Create books
book1 = Book("1984", "George Orwell")
book2 = Book("Brave New World", "Aldous Huxley")
book3 = Book("Animal Farm", "George Orwell")

# Put books in a list and sort them by title
book_list = [book1, book2, book3]
sorted_books = sorted(book_list)

# Output the sorted books
for book in sorted_books:
    print(book)
