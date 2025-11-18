class Vehicle:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
        print('Vehicle initialized')

class Car(Vehicle):
    def __init__(self,brand,color,model):
        super().__init__(brand,color)
        self.model=model
        print('Car initialized')
        
mycar=Car('Toyota','red','Fortuner')
print(mycar.brand)
print(mycar.model)
print(mycar.color)
