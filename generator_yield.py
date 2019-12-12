def even_num(n):
    for i in range(1,n+1):
        if i % 2 == 0:
            yield(i)
for i in even_num(20):
    print(i)