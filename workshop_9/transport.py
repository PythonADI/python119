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
