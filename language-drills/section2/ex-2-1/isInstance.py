def uppercase_if_string(value):
    if isinstance(value, str): 
        return value.upper()
    else:
        return "Not a string"


print(uppercase_if_string("hello"))   
print(uppercase_if_string(42))        
