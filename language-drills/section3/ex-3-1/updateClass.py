class Book:
    # Class variable
    category = "Fiction"
    
    def __init__(self, title, author):
        self.title = title      
        self.author = author 

    def describe(self):
        return f"Title: {self.title}, Author: {self.author}, Category: {Book.category}"

    def update_title(self, new_title):
        self.title = new_title 


book = Book("The Great Adventure", "John Doe")


print(book.category)  


book.update_title("The New Adventure")


print(book.describe())  
