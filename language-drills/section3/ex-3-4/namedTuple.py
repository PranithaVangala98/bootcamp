from collections import namedtuple

# Define the Point namedtuple with x and y as fields
Point = namedtuple('Point', ['x', 'y'])

# Create an instance of Point
point1 = Point(3, 4)

# Access fields by name
print(f"Point coordinates: x={point1.x}, y={point1.y}")  # Output: x=3, y=4

# You can also access the fields by index, like a regular tuple
print(f"Point as tuple: {point1[0]}, {point1[1]}")  # Output: 3, 4
