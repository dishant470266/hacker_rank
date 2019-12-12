def my_sum(*args):
    if all([type(i) == int or type(i) == float for i in args]):
     total = 0
     for i in args:
        total += i
     return total
    else:
        return "worng output"
print(my_sum(1,2,3,4))