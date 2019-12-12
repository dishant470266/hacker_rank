# def is_palindrome(name):
#     reversed = name[::-1]
#     if name == reversed:
#      return True
#     else:
#      return False

# word = input("enter name : ")
# reverse = is_palindrome(word)
# print(reverse)

def is_palindrome(name):
    if name == name[::-1]:
     return True
    
    return False

word = input("enter name : ")
reverse = is_palindrome(word)
print(reverse)