# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} engine started.")

    def stop(self):
        print(f"{self.brand} {self.model} engine stopped.")


# Child class: Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Call Vehicle's constructor
        self.doors = doors

    def open_trunk(self):
        print(f"{self.brand} {self.model}'s trunk is now open.")

    def info(self):
        print(f"Car: {self.brand} {self.model}, Doors: {self.doors}")


# Child class: Bike inherits from Vehicle
class Bike(Vehicle):
    def __init__(self, brand, model, type_of_bike):
        super().__init__(brand, model)
        self.type_of_bike = type_of_bike

    def do_wheelie(self):
        print(f"{self.brand} {self.model} is doing a wheelie!")

    def info(self):
        print(f"Bike: {self.brand} {self.model}, Type: {self.type_of_bike}")


# Using the classes
my_car = Car("Toyota", "Corolla", 4)
my_bike = Bike("Yamaha", "R15", "Sports")

# Car actions
my_car.info()
my_car.start()
my_car.open_trunk()
my_car.stop()

print()  # Just to separate outputs

# Bike actions
my_bike.info()
my_bike.start()
my_bike.do_wheelie()
my_bike.stop()
