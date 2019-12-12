# def add_two(a,b):
#     return(a+b)
# print(add_two(5,4))
#=========================================================
# def add_two(a,b):
#     return a+b
# a = int(input("enter first nummber : "))
# b = int(input("enter second nummber : "))

# total = add_two(a,b)
# print(total)
#=============================================================

# def last_letter(name):
#     return name[-1]

# print(last_letter("disha"))
# #====================================================
# def odd_even(num):
#     if num%2 == 0:
#         return "even"
#     return "odd"
# #print(odd_even(5))


# num = int(input("enter first number : "))

# result = odd_even(num)
# print(result)
#====================================================


# def is_even(num):
#     return num%2 == 0 
# print(is_even(5))

#==============================================


#ex. 1

# def greater(a,b):
#     if a > b:
#         return a
#     else:
#         return b

# num1 = int(input("enter first nummber : "))
# num2  = int(input("enter second nummber : "))

# bigger = greater(num1,num2)
# print(bigger)

#===============================================

def greater(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(greater(10,20,30))