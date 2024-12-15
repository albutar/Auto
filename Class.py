class Car:
    def __init__(self, model, year, engine_capacity, price, mileage):
        self.model = model
        self.year = year
        self.engine_capacity = engine_capacity
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def description(self):
        return (f"Model: {self.model}, Year: {self.year}, Engine Capacity: {self.engine_capacity}L, "
                f"Price: ${self.price}, Mileage: {self.mileage} km, Wheels: {self.wheels}")

car1 = Car(model="Toyota", year=2020, engine_capacity=1.8, price=5000, mileage=8000)

class Truck(Car):
    def __init__(self, model, year, engine_capacity, price, mileage):
        super().__init__(model, year, engine_capacity, price, mileage)
        self.wheels = 8

truck1 = Truck(model="FORD", year=2015, engine_capacity=12.8, price=20000, mileage=30000)

print(car1.description())
print(truck1.description())