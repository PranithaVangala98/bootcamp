from itertools import islice

def line_generator():
    for i in range(100):
        yield f"line {i}"

gen = line_generator()

#read first 10 lines
first_ten_lines = list(islice(gen, 10))

for line in first_ten_lines:
    print(line)
