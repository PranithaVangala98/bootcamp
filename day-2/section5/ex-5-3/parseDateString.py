from datetime import datetime

# Date string to be parsed
date_string = "2024-01-01"

# Parse the string into a datetime object
date_object = datetime.strptime(date_string, "%Y-%m-%d")

# Output the datetime object
print("Datetime object:", date_object)
