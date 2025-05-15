from datetime import datetime
import calendar

# Date string to be parsed
date_string = "2024-01-01"

# Parse the string into a datetime object
date_object = datetime.strptime(date_string, "%Y-%m-%d")

# Get the weekday name using calendar.day_name
weekday_name = calendar.day_name[date_object.weekday()]

# Output the weekday name
print("Weekday name:", weekday_name)
