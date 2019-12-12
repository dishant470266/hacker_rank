import random
winning_number = random.randint(1,100)
#winning_number = 47
guess = 1
number = int(input("enter the number b/w 1 to 100 : "))
game_over = False
while not game_over:
    if number == winning_number:
        print(f"you win and you guess the number {guess} time")
        game_over = True
    else:
        if number < winning_number:
            print("too low")
            guess += 1
            number = int(input("enter again : "))
        else:
            print("too high")
            guess += 1
            number = int(input("enter again : "))
        