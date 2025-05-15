import sys

list_comp = [x for x in range(1000000)]
gen_expr = (x for x in range(1000000))

print("List comprehension size:", sys.getsizeof(list_comp))
print("Generator expression size:", sys.getsizeof(gen_expr))
