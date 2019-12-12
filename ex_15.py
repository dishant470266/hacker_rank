def reverce_list(l):
    return[i[::-1] for i in l]
print(reverce_list(['abc','bvc']))


#if statement list comprehsion
names = [1,2,3,4,5,67,8,9,10]
name = [i for i in names if i%2==0]
print(name)
