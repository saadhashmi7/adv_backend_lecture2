class vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"brand: {self.brand}")

        
class Car(vehicle):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model = model

    def show_full(self):
        print(f"car: {self.model}, {self.brand}")

if __name__ == '__main__':
    my_car = Car("Ford", "Mustang")
    my_car.show_brand()
    my_car.show_full()