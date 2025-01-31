import random
import time

# Base class
class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed  # Speed in km/h
    
    def race_time(self, distance):
        """Calculate time taken to cover distance (in hours)"""
        return distance / self.speed
    
    def __str__(self):
        return f"{self.name} (Speed: {self.speed} km/h)"

# Derived classes
class SportsCar(Car):
    def __init__(self, name):
        super().__init__(name, random.randint(180, 250))

class Truck(Car):
    def __init__(self, name):
        super().__init__(name, random.randint(80, 120))

class Sedan(Car):
    def __init__(self, name):
        super().__init__(name, random.randint(120, 180))

# Race simulation
def race(cars, distance):
    print(f"Starting a race of {distance} km!\n")
    results = []
    
    for car in cars:
        time_taken = car.race_time(distance)
        results.append((time_taken, car))
        print(f"{car.name} completed the race in {time_taken:.2f} hours.")
        time.sleep(1)  # Simulate race delay
    
    results.sort()  # Sort by time (ascending)
    print("\n🏆 The winner is:", results[0][1].name, "🏁\n")

# Create car objects
cars = [SportsCar("Ferrari"), Truck("Volvo Truck"), Sedan("Toyota Camry"), SportsCar("Lamborghini")]

# Start race with a 500 km distance
race(cars, 500)
