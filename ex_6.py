name = input("plz enter your name : ")

# name.count("D") ,  name.count(name[0])
# name.count("i") ,  name.count(name[1])
# name.count("s") ,  name.count(name[2])
# name.count("h") ,  name.count(name[3])
# name.count("a") ,  name.count(name[4])
# name.count("n") ,  name.count(name[5])

# output
# D : 1
# i : 1
# s : 1
# h : 1
# a : 2
# n : 1
# a : 2
temp_var = " "
i = 0
while i < len(name):
    if name[i] not in temp_var:
     print(f"{name[i]} : {name.count(name[i])}")
    i += 1