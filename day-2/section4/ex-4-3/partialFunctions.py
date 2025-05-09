import functools

int_base_2 = functools.partial(int, base=2)

binary_value = int_base_2("1101")
print(binary_value)  
