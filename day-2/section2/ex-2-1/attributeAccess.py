class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'location','notfound')

print(x)

