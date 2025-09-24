# Base class
class Car:
    def __init__(self, brand, model, fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel   

    def drive(self, distance):
        fuel_needed = distance * 0.1  # assume 0.1 liter/km
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            print(f"{self.brand} {self.model} drove {distance} km. Remaining fuel: {self.fuel:.1f}L")
        else:
            print(f"Not enough fuel to drive {distance} km!")

    def refuel(self, amount):
        self.fuel += amount
        print(f"{self.brand} {self.model} refueled. Current fuel: {self.fuel:.1f}L")


# Subclass (Inheritance)
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model, fuel=0)  # electric car doesn’t use fuel
        self.battery = battery  # battery in %

    def drive(self, distance):
        battery_needed = distance * 2  # assume 2% battery per km
        if self.battery >= battery_needed:
            self.battery -= battery_needed
            print(f"{self.brand} {self.model} drove {distance} km. Remaining battery: {self.battery}%")
        else:
            print(f"Not enough battery to drive {distance} km!")

    def recharge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} recharged. Battery: {self.battery}%")


# Example usage
car1 = Car("Toyota", "Corolla", 20)
car1.drive(50)
car1.refuel(10)

tesla = ElectricCar("Tesla", "Model 3", 80)
tesla.drive(20)
tesla.recharge(30)
