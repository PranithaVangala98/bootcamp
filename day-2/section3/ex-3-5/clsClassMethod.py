from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

    @classmethod
    def from_string(cls, s: str) -> 'Book':
        """Class method to create a Book or subclass instance from a string."""
        title, author = s.split('|')
        return cls(title=title.strip(), author=author.strip())

@dataclass
class SpecialEditionBook(Book):
    edition: str  # Additional attribute for SpecialEditionBook

    @classmethod
    def from_string(cls, s: str) -> 'SpecialEditionBook':
        """Class method to create a SpecialEditionBook instance from a string."""
        # Assuming format: "Title|Author|Edition"
        parts = s.split('|')
        title, author, edition = parts[0].strip(), parts[1].strip(), parts[2].strip()
        return cls(title=title, author=author, edition=edition)

# Test the class method for both Book and SpecialEditionBook
book_str = "The Great Gatsby|F. Scott Fitzgerald"
special_edition_str = "The Great Gatsby|F. Scott Fitzgerald|First Edition"

book = Book.from_string(book_str)
special_edition_book = SpecialEditionBook.from_string(special_edition_str)

# Print the created instances
print(book)  # Output: Book(title='The Great Gatsby', author='F. Scott Fitzgerald')
print(special_edition_book)  # Output: SpecialEditionBook(title='The Great Gatsby', author='F. Scott Fitzgerald', edition='First Edition')
