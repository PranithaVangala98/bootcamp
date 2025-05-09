
with open('big.txt', 'r') as source_file:
    with open('stream_write_big.txt', 'w') as dest_file:
        for line in source_file:
            dest_file.write(line)
