#number reverce 
#number = [1,2,3,4]

# def reverse_list(l):
#     l.reverse()
#     return l

# def reverse_list(l):
#     return l[::-1]
# print(reverse_list(number))

#=====================================

def reverse(l):
    l_list = []
    for i in range(len(l)):
        popped_item = l.pop()
        l_list.append(popped_item)
    return l_list
number = [1,2,3,4]
print(reverse(number))