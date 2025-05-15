import contextlib

# Try to remove a file, but suppress the error if it doesn't exist
with contextlib.suppress(FileNotFoundError):
    # This won't raise an error if the file is missing
    with open('non_existent_file.txt') as f:
        print(f.read())
