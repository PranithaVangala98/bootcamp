thislist = [1, 2, 3, 4]
s = []

for i in thislist:
    if i**2 % 4 == 0:
        s.append(i**2)

print(s)
