#normal function

def add(a,b):
    return a+b
print(add(3,5))

#lambda function

add2 =  lambda a,b : a+b
print(add2(2,5))

#==================
#ex 
even = lambda a : a%2==0
print(even(2))

#====================================
#if_else

func = lambda s : True if len(s) > 5 else False
print(func('dadf'))

func2 = lambda s : len(s) > 5 
print(func2('abccdf'))