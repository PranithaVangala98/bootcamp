import json
from datetime import datetime

# Define a custom JSON encoder class
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        # If the object is a datetime, convert it to a string
        if isinstance(obj, datetime):
            return obj.isoformat()  # or any other format you prefer
        # If the object is not a datetime, use the default behavior
        return super().default(obj)

# Create a datetime object
now = datetime.now()

# Serialize the datetime object using the custom encoder
json_data = json.dumps({'current_time': now}, cls=CustomJSONEncoder)

# Output the serialized JSON string
print(json_data)
