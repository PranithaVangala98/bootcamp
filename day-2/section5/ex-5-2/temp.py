import tempfile

# Create a temporary file
with tempfile.NamedTemporaryFile(delete=False, mode='w+t') as temp_file:
    # Write some content to the temporary file
    temp_file.write("Hello, this is a temporary file.")
    
    # Get the name of the temporary file
    temp_file_name = temp_file.name
    print(f"Temporary file created: {temp_file_name}")

# Read the content of the temporary file (outside the `with` block since it was not auto-deleted)
with open(temp_file_name, 'r') as file:
    content = file.read()
    print(f"Content of temporary file: {content}")
