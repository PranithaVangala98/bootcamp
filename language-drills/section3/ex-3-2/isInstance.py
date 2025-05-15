class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre


# Create an instance of Novel
novel = Novel("Pride and Prejudice", "Jane Austen", "Romance")

# Check using isinstance
print(isinstance(novel, Novel))  # True
print(isinstance(novel, Book))  # True
