class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r})"

# Create an instance
book = Book("1984", "George Orwell")

# Print (calls __str__)
print("Using print():", book)

# Inspect in interpreter (calls __repr__)
print("Using repr():", repr(book))
