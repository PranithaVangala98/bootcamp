import json
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

    @classmethod
    def from_string(cls, s: str) -> 'Book':
        """Factory method to create a Book instance from a string formatted as 'Title|Author'."""
        title, author = s.split('|')
        return cls(title=title.strip(), author=author.strip())

    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        """Factory method to create a Book instance from a dictionary."""
        return cls(title=data.get('title'), author=data.get('author'))

    @classmethod
    def from_json(cls, json_str: str) -> 'Book':
        """Factory method to create a Book instance from a JSON string."""
        data = json.loads(json_str)
        return cls(title=data.get('title'), author=data.get('author'))

# Test the alternative constructors
book_str = "The Great Gatsby|F. Scott Fitzgerald"
book_dict = {"title": "1984", "author": "George Orwell"}
book_json = '{"title": "To Kill a Mockingbird", "author": "Harper Lee"}'

book1 = Book.from_string(book_str)
book2 = Book.from_dict(book_dict)
book3 = Book.from_json(book_json)

# Print the created Book instances
print(book1)  # Output: Book(title='The Great Gatsby', author='F. Scott Fitzgerald')
print(book2)  # Output: Book(title='1984', author='George Orwell')
print(book3)  # Output: Book(title='To Kill a Mockingbird', author='Harper Lee')
