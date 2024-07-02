class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print("vehicle started")


class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def start(self):
        print(f"{self.make} {self.model} with {self.doors} doors started")


class ElectricCar(Car):
    def __init__(self, make, model, doors, battery_range):
        super().__init__(make, model, doors)
        self.battery_range = battery_range

    def start(self):
        print(f"{self.make} {self.model} with {self.doors} doors and {self.battery_range}KM range started")


vehicle = Vehicle("Generic", "Model")
car = Car("Tata", "Nexon", 4)
electric_car = ElectricCar("BMW", "QC", 4, 410)

vehicle.start()
car.start()
electric_car.start()
