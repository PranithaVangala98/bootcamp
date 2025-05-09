# Define the Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Instantiate the Book object
book = Book("1984", "Orwell")

# Print the attributes of the book
print(f"Title: {book.title}")
print(f"Author: {book.author}")
