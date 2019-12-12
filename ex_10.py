def odd_even(l):
    odd_num = []
    even_num = []
    for i in l:
        if i % 2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)
    output = [odd_num,even_num]
    return output

number = [1,2,3,4,5,6,7,8,9]
print(odd_even(number))
print("\U0001F607")