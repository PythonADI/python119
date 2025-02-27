class Dog:
    # Dog is considered as a Parent class for RobotDog
    # we use TitleCase for class names
    def __init__(self, name, age):
        # init - short for initialize. sometimes called a constructor
        # this is a special method that is called when a new object is created
        # self is reffering to the object itself on which we are currently working on
        # we create attrbutes for each object
        self.name = name
        self.age = age

    def sit(self):
        # sit is a method. Acts excatly like a function but is defined inside a class
        # self is a reference to the object itself
        print(f"{self.name} is sitting")

    def move(self, room):
        print(f"{self.name} is moving to {room}")


class RobotDog(Dog):
    # RobotDog is considered as a Child class for Dog
    def __init__(self, name, AI, brand, model_number, can_jump=True):
        super().__init__(name, 0)
        self.AI = AI
        self.brand = brand
        self.model_number = model_number
        self.can_jump = can_jump

    def sit(self):
        # this method overrides the sit method in the Dog class
        print(f"{self.name} is sitting like a robot")


# let's create an object of the class RobotDog
dog = RobotDog("doggo", "Claude", "Samsung", 1)
print(dog.name)
# Don't Do this!!
# dog.age = 5
# print(dog.age)
print(f"{dog.model_number = }")
dog.sit()


dog2 = RobotDog("Brave", "OpenAI", "Samsung", 2, False)
dog2.sit()

dog2.move("Kitchen")

dog.name = "Barkly"
dog.move("Living Room")

print(f"{dog2.can_jump = }")
