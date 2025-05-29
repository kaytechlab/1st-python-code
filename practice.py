#You're building a basic software for a parking lot system.
#The lot handles different types of vehicles — Cars, Bikes, and Trucks.
# Each vehicle type has a different parking fee. As the lot gets busier,
#managing these differences with just conditionals is getting messy and hard to scale.
#Your goal is to design a system that makes it easy to add
#new vehicle types later, and each vehicle knows how much to charge for parking — without using if statements everywhere.
#Your Task:
#Create a base class called Vehicle.
#Create three subclasses: Car, Bike, and Truck.
#Each subclass should define its own parking_fee() method that returns the fee for that type:
#Car: 20
#Bike: 10
#Truck: 40
#Write a small program that:
#Creates one object of each type
#Stores them in a list
#Loops through the list and prints the parking fee for each

# Step 1: Create a base class for all vehicles
class Vehicle:
    def parking_fee(self):
        pass

# Step 2: Create subclasses for Car, Bike, and Truck
class Car(Vehicle):
    def parking_fee(self):
        return 20

class Bike(Vehicle):
    def parking_fee(self):
        return 10

class Truck(Vehicle):
    def parking_fee(self):
        return 40

# Step 3: Create objects for each vehicle
car = Car()
bike = Bike()
truck = Truck()

# Step 4: Store them in a list and display parking fee
vehicles = [car, bike, truck]

for vehicle in vehicles:
    print(f"{vehicle.__class__.__name__} parking fee is ₦{vehicle.parking_fee()}")
