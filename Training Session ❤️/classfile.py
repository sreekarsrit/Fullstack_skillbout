class Vehicle:
    def __init__(self,price,name):
        self.name=name
        self.price=price

    def getname(self):
        return(self.name)
    def getprice(self):
        return(self.price)

vehicle1=Vehicle(name="toyota",price="300000")
vehicle2=Vehicle(name="bmw",price="900000")
print(vehicle1.getname())
print(vehicle1.getprice())
print(vehicle2.getname())
print(vehicle2.getprice())