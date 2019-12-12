class Laptop:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

laptop1 = Laptop('HP','alu1x2',45000)

print(laptop1.model)