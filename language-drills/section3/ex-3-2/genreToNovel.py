class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"'{self.title}' by {self.author}")


class Novel(Book):
    def __init__(self, title, author, genre):
        # Call the parent constructor
        super().__init__(title, author)
        # Add new attribute
        self.genre = genre

    def describe(self):
        # Extend the parent describe method
        super().describe()
        print(f"Genre: {self.genre}")


# Test the Novel class
novel = Novel("1984", "George Orwell", "Dystopian")
novel.describe()
