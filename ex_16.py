def square_num(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "you did't pass any value"
num1 = [1,2,3]
print(square_num(2,*num1))