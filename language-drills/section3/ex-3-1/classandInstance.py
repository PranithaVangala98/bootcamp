class Book:
    # Class variable
    category = "Fiction"

    def __init__(self, title, author):
        self.title = title  
        self.author = author  

    def describe(self):
        return f"The book '{self.title}' is written by {self.author}."


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")


print(book1.category)  


print(Book.category) 
