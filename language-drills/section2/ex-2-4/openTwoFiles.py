with open('example.txt', 'r') as infile, open('outputfile.txt', 'w') as outfile:
    # Read from input file and write to output file
    data = infile.read()
    outfile.write(data)

print("Data copied from input.txt to output.txt.")