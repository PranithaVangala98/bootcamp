class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"Book: {self.title} by {self.author}"


class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def describe(self):
        return f"Novel: {self.title} by {self.author}, Genre: {self.genre}"


novel_obj = Novel("1984", "George Orwell", "Dystopian")

print(novel_obj.describe())
