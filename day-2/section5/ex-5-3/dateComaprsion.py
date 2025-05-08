from datetime import datetime

# Define two date strings
date_string1 = "2024-01-01"
date_string2 = "2025-01-01"

# Parse the strings into datetime objects
date1 = datetime.strptime(date_string1, "%Y-%m-%d")
date2 = datetime.strptime(date_string2, "%Y-%m-%d")

# Compare the dates and print the result
if date1 < date2:
    print(f"{date_string1} is earlier than {date_string2}")
elif date1 > date2:
    print(f"{date_string1} is later than {date_string2}")
else:
    print(f"{date_string1} and {date_string2} are the same")
