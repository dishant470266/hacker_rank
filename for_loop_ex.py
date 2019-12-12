# total = 0
# for i in range(1,11):
#     total += i
# print(total)
    

# n = int(input("enter number"))
# total = 0
# for i in range(1,n+1):
#     total += i
# print(total)


# total = 0
 
# n = input("enter number")
# for i in range(0,len(n)):
#     total += int(n[i])
# print(total)

temp = " "

name = input("enter your name : ")

for i in range(0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]