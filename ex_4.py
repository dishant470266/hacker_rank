user_name = input("enter your name : ")
user_age = int(input("enter your age : "))
if(user_age >= 10 and user_name[0] == 'a' or user_name[0] == 'A' ):
    print("you can watch movie")
else:
    print("you can't watch this movie")
