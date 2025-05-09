class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __bool__(self):
        return self.available  # Consider the book "True" if it's available, else "False"

# Create books
book1 = Book("1984", "George Orwell", True)
book2 = Book("Brave New World", "Aldous Huxley", False)

# Test boolean context
print(bool(book1))  # Output: True (because book1 is available)
print(bool(book2))  # Output: False (because book2 is not available)

# Test in an if statement
if book1:
    print(f"{book1} is available.")
else:
    print(f"{book1} is not available.")

if book2:
    print(f"{book2} is available.")
else:
    print(f"{book2} is not available.")
