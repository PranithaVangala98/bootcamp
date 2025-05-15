def flat(lis):
    flatList = []
    for element in lis:
        if type(element) is list:
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList


lis = [[1, 2], [3, 4]]
print("List", lis)
print("Flat List", flat(lis))
