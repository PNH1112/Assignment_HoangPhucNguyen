import random
MIN_RAND_SPEED = -10
MAX_RAND_SPEED = 15

class Car():
    def __init__(self,registerNo,maxSpd):

        self.registerNo = registerNo
        self.maxSpeed = maxSpd
        self.currentSpd = 0
        self.distance = 0

    def __str__(self):
        return f"""Number: {self.registerNo} | Max Speed: {self.maxSpeed} | Current Speed: {self.currentSpd} | Travelled Distance: {self.distance}"""


    def speed(self,changeSpeed):

        self.currentSpd =  self.currentSpd + changeSpeed
        if self.currentSpd < 0:
             self.currentSpd = 0
        elif self.currentSpd >= self.maxSpeed:
            self.currentSpd = self.maxSpeed
        return

    def acceleration(self):
        randomChangeSpeed = random.randint(MIN_RAND_SPEED,MAX_RAND_SPEED)
        self.speed(randomChangeSpeed)


    def drive(self,time):
        self.distance = self.distance + self.currentSpd * time

    def consume(self):
        pass

if  __name__ == "__main__":


    carList = []
    for i in range(2):
        car = Car("ABC",123)
        carList.append(car)

    print(carList)