class Laptop:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def apply_discount(self,num):
        off_price = (num/100)*self.price
        return self.price - off_price

laptop1 = Laptop('HP','alu1x2',45000)
print(laptop1.apply_discount(10))
