
"""
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