def make_doubler():
    def doubler(x):
        return x * 2
    return doubler

doubler_func = make_doubler()
result = doubler_func(5)
print(result)  
