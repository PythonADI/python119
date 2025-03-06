from vehicles import Carriage, Car
from planes import SpaceShip

indiana_jones = Carriage("Ford", "Model T", 1915, 1000)
indiana_jones.start()
indiana_jones.move()

batmobile = Car("Ford", "Mustang", 1967, 10000)
batmobile.start()

apollo_11 = SpaceShip("NASA", "Apollo 11", 1969, 1000000)
apollo_11.start()
apollo_11.move()
