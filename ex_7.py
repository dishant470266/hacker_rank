number = [1,2,3,4,5,6]

def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square
print(square_list(number))
    