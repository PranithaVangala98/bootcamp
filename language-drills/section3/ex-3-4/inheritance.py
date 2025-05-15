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

# Create an instance of AdminUser
admin1 = AdminUser(name="Alice", age=30, access_level="SuperAdmin")

# Print the AdminUser instance
print(admin1)  # Output: AdminUser(name='Alice', age=30, access_level='SuperAdmin')

# Test the inherited method
print(f"Is {admin1.name} an adult? {admin1.is_adult()}")  # Output: True
