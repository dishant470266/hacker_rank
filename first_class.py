#__init__,self
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('abc','cvb',21)
p2 = Person('jkl','bcv',20)

print(p1.first_name)
print(p2.first_name)
