# num1 = input("enter first number")
# num2 = input("enter second number")
# num3 = input("enter third number")
#(int(num1) + int(num2) + int(num3) )

num1,num2,num3 = input("enter three number").split(",")



print(f"three number average : {((int(num1) + int(num2) + int(num3) ) / 3)}")