class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"Book: '{self.title}' by {self.author}")


class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def describe(self):
        print(f"Novel: '{self.title}' by {self.author} (Genre: {self.genre})")


# Create instances
book = Book("Sapiens", "Yuval Noah Harari")
novel = Novel("The Great Gatsby", "F. Scott Fitzgerald", "Classic Fiction")

# Polymorphic behavior in action
library = [book, novel]

for item in library:
    item.describe()
