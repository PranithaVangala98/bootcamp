def read_large_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line

# Usage example
for line in read_large_file('big.txt'):
    # Process each line
    print(line.strip())