a = [1, 2, 3, 4, 5]

c = [0, 7, 5, 6, 2]


def copyThroughAssignment(a):
    b = a
    b.append(7)
    print("a", a)
    print("b", b)


def copyThrougthColon(a):
    b = a[:]
    b.append(6)
    print(b)
    print(a)


copyThroughAssignment(a)
copyThrougthColon(c)
