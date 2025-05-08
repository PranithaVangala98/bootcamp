class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Test equality
book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")
book3 = Book("Animal Farm", "George Orwell")

print(book1 == book2)  # True
print(book1 == book3)  # False
print(book1 == "not a book")  # False
