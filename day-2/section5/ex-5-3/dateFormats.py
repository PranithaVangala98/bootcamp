from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Format the current date as "YYYY-MM-DD"
formatted_date = current_datetime.strftime("%Y-%m-%d")

# Print the formatted date
print("Formatted Date:", formatted_date)
