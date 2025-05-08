thisdict = { 'name':'pranitha', 'location':'hyderabad'}

try:
    value = thisdict["age"]
except KeyError:
    print('Value is not present')
