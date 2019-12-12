def add(a,b):
    if (type(a) is int and type(b) is int):
        return a + b
    raise TypeError('oops worng data type')
print(add(2,4))