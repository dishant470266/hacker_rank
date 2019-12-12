number = [1,32,3,4,5,6,7,6,6]

def nagative_list(l):
    nagative = []
    for i in l:
        nagative.append(-i)
    return nagative
print(nagative_list(number))