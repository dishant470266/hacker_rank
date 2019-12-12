name,char = input("enter your name and char  : ").split(",")
print(f"lenght of your name {len(name)}")
#print(f"character count : {name.lower().count(char.lower())}")     # case sensitive


print(f"character count : {name.strip().lower().count(char.strip().lower())}")


#sname.strip().lower().count(char.strip().lower())
