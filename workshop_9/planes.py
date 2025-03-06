from transport import Transport

class Plane(Transport):
    def move(self):
        print(f"{self.brand} {self.model} is flying in the sky")


class SpaceShip(Transport):
    def move(self):
        print(f"{self.brand} {self.model} is flying in the space")
