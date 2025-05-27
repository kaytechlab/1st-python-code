# # object orientated programming in python

string = "hello"
print(string.upper())

class Dog:
    def bark(self):
        print("bark")

d = Dog()
d.bark()
print(type(d))

# Define the class
class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name}: ₦{self.price}")

# Inherit from FoodItem
class ComboMeal(FoodItem):
    def __init__(self, name, price, items):
        super().__init__(name, price)
        self.items = items  # list of food items in the combo

    def display(self):
        print(f"Combo - {self.name}: ₦{self.price}")
        print("Includes:")
        for item in self.items:
            print(f" - {item}")

# Customer class to place an order
class Customer:
    def __init__(self, name):
        self.name = name
        self.order = []

    def add_to_order(self, food_item):
        self.order.append(food_item)
        print(f"{food_item.name} added to {self.name}'s order.")

    def checkout(self):
        total = sum(item.price for item in self.order)
        print(f"\n{self.name}'s Order Summary:")
        for item in self.order:
            item.display()
        print(f"Total: ₦{total}")

# Using the classes
rice = FoodItem("Jollof Rice", 1200)
chicken = FoodItem("Grilled Chicken", 1500)
combo = ComboMeal("Rice & Chicken Combo", 2500, ["Jollof Rice", "Grilled Chicken", "Plantain"])

customer1 = Customer("Ada")
customer1.add_to_order(rice)
customer1.add_to_order(chicken)
customer1.add_to_order(combo)

customer1.checkout()

def add_student(self, student):
    if len(self.students) < self.max_students:
        self.students.append(student)
