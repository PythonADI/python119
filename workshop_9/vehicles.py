from transport import Transport

class Vehicle(Transport):
    def move(self):
        print(f"{self.brand} {self.model} is moving on the land")


class Car(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is moving on the road with the help of an engine")


class Carriage(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is moving on the road with the help of horses")
