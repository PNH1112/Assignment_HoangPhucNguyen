# 1,2,3

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

# 4
import random
class Car:
    def __init__(self, registration_number: str, maximum_speed: int, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def time_drive(self, time):
        self.travelled_distance += self.current_speed * time


class Race:
    def __init__(self):
        self.carlist = []
        for i in range(1, 11):
            registration_number = f"ABC-{i}"
            maximum_speed = random.randint(100, 200)
            car = Car(registration_number, maximum_speed)
            self.carlist.append(car)
            print(f"{registration_number} have maximum speed {maximum_speed}")

    def drive(self, hour):
        for a in self.carlist:
            self.hour = hour
            change_speed = random.randint(-10, 15)
            a.accelerate(change_speed)
            a.time_drive(hour)

    def WIN(self):
        for car in self.carlist:
            if car.travelled_distance > 10000:
                return car


Pixel = Race()
hour = 1
winner = None
while winner is None:
    Pixel.drive(1)
    print("___________________________________________________________________________")
    print(f"Hour {hour}")
    print()
    hour += 1
    winner = Pixel.WIN()
    for car_race in Pixel.carlist:
        print(
            f"Car: {car_race.registration_number} - Max Speed: {car_race.maximum_speed} - Current Speed {car_race.current_speed}"
            f" - Travelled distance: {car_race.travelled_distance}")

if winner:
    print()
    print(f"The winner is Car {winner.registration_number}!")
    print(f"Maximum Speed: {winner.maximum_speed} km/h")
    print(f"Current Speed: {winner.current_speed} km/h")
    print(f"Travelled Distance: {winner.travelled_distance} km")
    print()
    print(f"Information table")
for car_information in Pixel.carlist:
    print(f"Car: {car_information.registration_number} - Max speed: {car_information.maximum_speed} - "
          f"Current speed: {car_information.current_speed} - Travelled distance: {car_information.travelled_distance}")
