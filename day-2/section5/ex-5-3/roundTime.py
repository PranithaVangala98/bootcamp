from datetime import datetime, timedelta

# Get the current datetime
current_time = datetime.now()

# Round to the next hour by adding the difference to the next hour
rounded_time = (current_time + timedelta(hours=1)).replace(
    minute=0, second=0, microsecond=0
)

# Output the rounded time
print("Rounded time to the top of the hour:", rounded_time)
