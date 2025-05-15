from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

    def is_adult(self) -> bool:
        """Returns True if age is 18 or greater, indicating an adult."""
        return self.age >= 18

@dataclass
class AdminUser(User):
    access_level: str  # New attribute for admin users

    @staticmethod
    def validate_isbn(isbn: str) -> bool:
        """Validate if the string is a valid ISBN-10 or ISBN-13."""
        # Remove hyphens if present
        isbn = isbn.replace("-", "")

        # ISBN-10 validation (10 digits, check digit can be 'X' for 10)
        if len(isbn) == 10 and isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X'):
            return True
        
        # ISBN-13 validation (13 digits, all must be digits)
        if len(isbn) == 13 and isbn.isdigit():
            return True
        
        return False

# Test the static method
print(AdminUser.validate_isbn("123-456-789-X"))  # Output: True (valid ISBN-10)
print(AdminUser.validate_isbn("978-3-16-148410-0"))  # Output: True (valid ISBN-13)
print(AdminUser.validate_isbn("123456789"))  # Output: False (invalid ISBN)
