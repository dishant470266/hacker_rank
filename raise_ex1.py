class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        raise NotImplementedError('you have to define in this method')

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    
    def sound(self):
        return  'bhow bhow'

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    
    
    def sound(self):
        return  'meao meao'

doggy = Dog('boony','pug')
catee = Cat('kitee','gen')
print(doggy.sound())
print(catee.sound())