import tempfile

# Create a temporary file in binary mode (can also use mode='w+' for text)
with tempfile.TemporaryFile(mode='w+t') as tmp:
    # Write some data to the temp file
    tmp.write("Hello, temporary file!\nAnother line.")
    
    # Go back to the beginning to read what was written
    tmp.seek(0)
    
    # Read and print the content
    content = tmp.read()
    print(content)

# File is automatically deleted after the block
