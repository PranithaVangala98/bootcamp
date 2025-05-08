from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

    @classmethod
    def from_string(cls, s: str) -> 'Book':
        """Class method to create a Book instance from a string."""
        title, author = s.split('|')
        return cls(title=title.strip(), author=author.strip())

# Test the class method
book_str = "The Great Gatsby|F. Scott Fitzgerald"
book = Book.from_string(book_str)

# Print the created Book instance
print(book)  # Output: Book(title='The Great Gatsby', author='F. Scott Fitzgerald')
