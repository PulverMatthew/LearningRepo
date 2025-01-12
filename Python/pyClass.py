# Initializes a class. Classes allow for encapsulation of data for reuse and readability.
class Vehicle():
    # Initialization function in class. Includes parameter bodyStyle.
    def __init__(self, bodyStyle, fuel = 10):
        # Object variable. Defined by the class' parameters.
        self.bodyStyle = bodyStyle
        self.fuel = fuel
    
    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed
        # Modified drive method to complete exercise.
        if self.fuel == 0:
            print("This vehicle cannot drive anymore as it is out of fuel!")
        else:
            self.fuel = self.fuel - 1 

    
# Put the superclass name in a subclass 
class Car(Vehicle):
    def __init__(self, engineType):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engineType = engineType

    def drive(self, speed):
        super().drive(speed)
        if self.fuel > 0:
            print("Driving my", self.engineType, "car at", self.speed)

# Truck subclass for exercise as suggested by Copilot.
class Truck(Vehicle):
    def __init__(self, engineType, cargoCapacity):
        super().__init__("Truck")
        self.wheels = 4
        self.doors = 4
        self.engineType = engineType
        # Requested cargo capacity attribute.
        self.cargoCapacity = cargoCapacity
    
    # Requested drive method. Has same functionality as other subclasses.
    def drive(self, speed):
        super().drive(speed)
        if self.fuel > 0:
            print("Driving my", self.engineType, "truck at", self.speed)



# Another subclass.
class Motorcycle(Vehicle):
    def __init__(self, engineType, hasSideCar):
        super().__init__("Motorcycle")
        if hasSideCar:
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.engineType = engineType

    def drive(self, speed):
        super().drive(speed)
        if self.fuel > 0:
            print("Driving my", self.engineType, "motorcycle at", self.speed)


    

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)
truck1 = Truck("diesel", 100)
truck2 = Truck("electric", 50)

#Test prints
print(mc1.wheels)
print(car1.engineType)
print(car2.doors) 

#Test calls
car1.drive(30)
car2.drive(40)
mc1.drive(50)

#Truck test. Runs drive 11 times then prints cargo capacity of the two truck objects.
for x in range(0,11):
    truck1.drive(50)
print(truck1.cargoCapacity)
print(truck2.cargoCapacity)