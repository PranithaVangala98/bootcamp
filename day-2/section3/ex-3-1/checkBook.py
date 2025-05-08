class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


book_obj = Book("The Great Gatsby", "F. Scott Fitzgerald")


if isinstance(book_obj, Book):
    print("The object is a Book.")
else:
    print("The object is NOT a Book.")
