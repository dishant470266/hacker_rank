Winning_number = 27
user_input = int(input("guess a number b/w 1 and 100 : "))
if(user_input == Winning_number):
    print("You Win!!!")
    print("\U0001F602")
else:
    if(user_input < Winning_number):
        print("too low")
    else:
        print("low high")