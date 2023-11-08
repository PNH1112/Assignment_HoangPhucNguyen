#123
"""
import random
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = 1
        self.to_floor = None

    def go_to_floor(self, to_floor):
        if self.bottom <= to_floor <= self.top:
            self.to_floor = to_floor
            print(f"The elevator is currently at floor {self.current_floor}")
            print(f"The elevator is going to floor {to_floor}")
            self.move_elevator()
        else:
            print(f"We don't have floor {to_floor}")

    def move_elevator(self):
        while self.current_floor != self.to_floor:
            if self.current_floor < self.to_floor:
                self.floor_up()
            elif self.current_floor > self.to_floor:
                self.floor_down()
        print(f"The current floor is {self.current_floor}")
        print()

    def floor_up(self):
        self.current_floor += 1
        print("The elevator is going up")
        print(f"Floor {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print("The elevator is going down")
        print(f"Floor {self.current_floor}")

class Building:
    def __init__(self, all_elevators, bottom, top):
        self.all_elevators = all_elevators
        self.elevators = []

        for i in range(self.all_elevators):
            i = Elevator(1,random.randint(7,10))
            self.elevators.append(i)
    def move_all(self, destination_floor):
        for abc in self.elevators:
            abc.go_to_floor(destination_floor)

    def fire_alarm(self):
        for abc in self.elevators:
            abc.go_to_floor(1)


Eve = Elevator(1,10)
Eve.go_to_floor(5)
Eve.go_to_floor(1)

B1 = Building(2, 1, 10)
B1.move_all(7)
B1.fire_alarm()
"""
#4
import random

class Car:
    def __init__(self, registration_number: str, maximum_speed: int, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def time_drive(self, time):
        self.travelled_distance += self.current_speed * time

class Race:
    def __init__(self, name, km, carlist):
        self.name = name
        self.km = km
        self.carlist = carlist

    def hour_passes(self, hour):
        for car in self.carlist:
            change_speed = random.randint(-10, 15)
            car.accelerate(change_speed)
            car.time_drive(hour)

    def race_finished(self):
        for car in self.carlist:
            if car.travelled_distance >= self.km:
                return True
        return False

    def print_status(self):
        print("Current Race Status:")
        for car_race in self.carlist:
            print(
                f"Car: {car_race.registration_number} - Max Speed: {car_race.maximum_speed} - Current Speed: {car_race.current_speed}"
                f" - Travelled distance: {car_race.travelled_distance} km")
        print("------------------------------------------------------------")

def main():
    carlist = []
    for i in range(1, 11):
        registration_number = f"ABC-{i}"
        maximum_speed = random.randint(100, 200)
        car = Car(registration_number, maximum_speed)
        carlist.append(car)
        print(f"Car {registration_number}'s maximum speed is: {maximum_speed} km/h")

    grand_demolition_derby = Race("Grand Demolition Derby", 8000, carlist)

    hour = 1
    while not grand_demolition_derby.race_finished():
        grand_demolition_derby.hour_passes(1)
        if hour % 10 == 0:
            print(f"Hour {hour}")
            grand_demolition_derby.print_status()
        hour += 1

    print("\nRace Finished!")

    winner = None
    for car in grand_demolition_derby.carlist:
        if car.travelled_distance >= grand_demolition_derby.km:
            winner = car
            break

    if winner:
        print(f"The winner is Car {winner.registration_number}!")
        print(f"Maximum Speed: {winner.maximum_speed} km/h")
        print(f"Current Speed: {winner.current_speed} km/h")
        print(f"Travelled Distance: {winner.travelled_distance} km")
        print("\nInformation table:")
        print(f"\nRace finished at hour {hour}")
        for car_information in grand_demolition_derby.carlist:
            print(f"Car: {car_information.registration_number} - Max speed: {car_information.maximum_speed} - "
                  f"Current speed: {car_information.current_speed} - Travelled distance: {car_information.travelled_distance} km")

if __name__ == "__main__":
    main()

