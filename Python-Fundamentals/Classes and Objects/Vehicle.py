class Vehicle:
    def __init__(self, model_type, model, price, owner=None):
        self.type = model_type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money, owner):
        if money < self.price:
            return f"Sorry, not enough money"
        elif self.owner is not None:
            return f"Car already sold"

        self.owner = owner
        change = money - self.price
        return f"Successfully bought a {self.type}. Change: {change:.2f}"

    def sell(self):
        if self.owner is None:
            return f"Vehicle has no owner"

        self.owner = None

    def __repr__(self):
        if self.owner is None:
            return f"{self.model} {self.type} is on sale: {self.price}"

        return f"{self.model} {self.type} is owned by: {self.owner}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)