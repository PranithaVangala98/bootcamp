class SafeObject:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        
        print(f"Attribute '{attr}' not found, returning fallback.")
        return f"<Missing: {attr}>"


obj = SafeObject("Example")

print(obj.name)       
print(obj.age)         
print(obj.title)       
