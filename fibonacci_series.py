def fibonacci(n):
    a = 0 
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(b)
    else:
        print(a,b, end = " ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(b, end = " ")

print(fibonacci(10))