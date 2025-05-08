from datetime import datetime, timedelta

# Get the current date and time
current_datetime = datetime.now()

# Add 7 days to the current date
new_datetime = current_datetime + timedelta(days=7)

# Print the new date and time
print("Current Date and Time:", current_datetime)
print("New Date and Time after adding 7 days:", new_datetime)
