from collections import namedtuple

# Define the Point namedtuple with invalid field names
Point = namedtuple('Point', ['x-coordinate', 'y-coordinate', '1st_point'])

# Create an instance of Point
point1 = Point(3, 4, 'Origin')

# Access the renamed fields
print(f"Point coordinates: {point1.x_coordinate}, {point1.y_coordinate}, {point1._1st_point}")
