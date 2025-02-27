class Transport:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def start(self):
        print(f"{self.brand} {self.model} is starting")

    def move(self):
        print(f"{self.brand} {self.model} is Moving")


class Vehicle(Transport):
    def move(self):
        print(f"{self.brand} {self.model} is moving on the land")


class Car(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is moving on the road with the help of an engine")


class Carriage(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is moving on the road with the help of horses")


class Plane(Transport):
    def move(self):
        print(f"{self.brand} {self.model} is flying in the sky")


class SpaceShip(Transport):
    def move(self):
        print(f"{self.brand} {self.model} is flying in the space")



indiana_jones = Carriage("Ford", "Model T", 1915, 1000)
indiana_jones.start()
indiana_jones.move()
