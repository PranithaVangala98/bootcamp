class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"'{self.title}' by {self.author}")

    def __str__(self):
        return f"Book: '{self.title}' by {self.author}"


class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def describe(self):
        super().describe()
        print(f"Genre: {self.genre}")

    def __str__(self):
        return f"Novel: '{self.title}' by {self.author} (Genre: {self.genre})"


# Test the __str__ method
book = Book("To Kill a Mockingbird", "Harper Lee")
novel = Novel("1984", "George Orwell", "Dystopian")

print(book)
print(novel)
