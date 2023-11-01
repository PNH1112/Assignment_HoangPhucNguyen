#1,2,3
"""
class Car:
    def __init__(self, registration_number: str, maximum_speed: int, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, acce):
        self.acce = acce
    def change_speed(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
    def brake(self, brake):
        self.current_speed += brake
        if self.current_speed < self.maximum_speed:
            self.current_speed = 0
    def time_drive(self, time):
        self.travelled_distance += self.current_speed * time

car1 = Car("ABC-123", 142)
print("Registration number:", car1.registration_number)
print("Maximum speed:", car1.maximum_speed)
print("Current speed:", car1.current_speed)
print("Travelled distance:", car1.travelled_distance)
car1.change_speed(30)
car1.change_speed(50)
car1.change_speed(70)
print("Current speed after acceleration:", car1.current_speed)
car1.time_drive(30)
car1.time_drive(20)
print(f"Total distance the {car1.registration_number} had travelled: {car1.travelled_distance}km")
car1.brake(-200)
print("Current speed after break:", car1.current_speed)
"""
#4
import random

class Car:
    def __init__(self, registration_number: str, maximum_speed: int, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, acce):
        self.acce = acce
    def change_speed(self, change):
        self.current_speed += change
        if self.current_speed < 0 :
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
    def time_drive(self, time):
        self.travelled_distance += self.current_speed * time
class CarRace:
    def __init__(self):
        self.cars = []
        for i in range(1, 11):
            registration_number = f"ABC-{i}"
            maximum_speed = random.randint(100, 200)
            car = Car(registration_number, maximum_speed)
            self.cars.append(car)
            print(f"Maximum speed of {registration_number} is {maximum_speed}")
    def race(self, hours):
        for car in self.cars:
            change_speed = random.randint(-10, 15)
            car.change_speed(change_speed)
            car.time_drive(hours)

    def check_winner(self):
        for car in self.cars:
            if car.travelled_distance >= 10000:
                return car


race_simulation = CarRace()
hour = 1
winner = None

while winner is None:
    race_simulation.race(1)
    winner = race_simulation.check_winner()
    print(f"Race Hour {hour}:")
    for car in race_simulation.cars:
        print(f"Car {car.registration_number} - Speed: {car.current_speed} km/h, Distance: {car.travelled_distance} km")
    hour += 1

if winner:
    print(f"The winner is Car {winner.registration_number}!")
    print(f"Maximum Speed: {winner.maximum_speed} km/h")
    print(f"Current Speed: {winner.current_speed} km/h")
    print(f"Travelled Distance: {winner.travelled_distance} km")

