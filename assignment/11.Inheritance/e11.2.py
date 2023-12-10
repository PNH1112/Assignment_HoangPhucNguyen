# Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar.
# Electric cars have the capacity of the battery in kilowatt-hours as their property.
# Gasoline cars have the volume of the tank in liters as their property.
# Write initializers for the subclasses. For example, the initializer of electric cars receives the registration number,
# maximum speed and battery capacity as its parameter. It calls the initializer of the base class to set the first two properties and then sets its capacity.
# Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l).
# Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.

from Car import Car


# def __init__(self, registerNo, maxSpd):
CONSUME_RATE = 10 ## can be 10Kh/100km or 10l/100km
TRAVELLED_DISTANCE_PER_UNIT = 100/ CONSUME_RATE ## 10KM/LITTER OR 10KM/1Kh
class GasolineCar(Car):
    consume_rate = CONSUME_RATE
    def __init__(self,registerNo,maxSpd,battery):
        super().__init__(registerNo,maxSpd)
        self.battery = battery
        self.current_fuel = battery

    def __str__(self):
        origin = super().__str__()
        more_str = f' | BATTERY: {self.battery} | Current Battery Level: {self.current_fuel}'
        return origin + more_str

    def expected_fuel(self,time):
        expected_distance = self.currentSpd * time
        expected_consume_fuel = expected_distance / TRAVELLED_DISTANCE_PER_UNIT
        return expected_consume_fuel
    # consume fuel in 1 hour
    def is_enough_Fuel(self,time):
        expected_consume_fuel = self.expected_fuel(time)
        if expected_consume_fuel <= self.current_fuel:
            return True
        else:
            return False

    def required_fuel(self,time):
        expected_consume_fuel = self.expected_fuel(time)
        # print(self.is_enough_Fuel(time))
        if self.is_enough_Fuel(time):
            required_fuel = expected_consume_fuel
        else:
            required_fuel = self.current_fuel
        return  required_fuel


    def consume(self,time):
        required_fuel = self.required_fuel(time)
        self.current_fuel = round(self.current_fuel - required_fuel,2)
        ## if expected consumed fuel <= current tank_level >> decreace tank level  >> return expected consumed fuel
        ## if expected consumed fuel > current tank_level >> empty tank level >> return the current tank level before empty
        return

#if fuel is not enough, distance based on remaining fuel
    def drive(self,time):
        required_fuel = self.required_fuel(time)
        self.distance = required_fuel * TRAVELLED_DISTANCE_PER_UNIT
        self.consume(time)



class EletricCar(Car):

    consume_rate = CONSUME_RATE

    def __init__(self,registerNo, maxSpd, tank):
        super().__init__(registerNo,maxSpd)
        self.tank = tank
        self.current_fuel = tank

    def __str__(self):
        origin = super().__str__()
        more_str = f' | Tank: {self.tank} | Current Tank Level: {self.current_fuel}'
        return origin + more_str

        expected_distance = self.currentSpd * time
        expected_consume_fuel = expected_distance / TRAVELLED_DISTANCE_PER_UNIT
        return expected_consume_fuel

    def expected_fuel(self,time):
        expected_distance = self.currentSpd * time
        expected_consume_fuel = expected_distance / TRAVELLED_DISTANCE_PER_UNIT
        return expected_consume_fuel
    # consume fuel in 1 hour
    def is_enough_Fuel(self, time):
        expected_consume_fuel = self.expected_fuel(time)
        if expected_consume_fuel <= self.current_fuel:
            return True
        else:
            return False

    def required_fuel(self, time):
        expected_consume_fuel = self.expected_fuel(time)
        # print(self.is_enough_Fuel(time))
        if self.is_enough_Fuel(time):
            required_fuel = expected_consume_fuel
        else:
            required_fuel = self.current_fuel
        return required_fuel

    def consume(self, time):
        required_fuel = self.required_fuel(time)
        self.current_fuel = round(self.current_fuel - required_fuel, 2)
        ## if expected consumed fuel <= current tank_level >> decreace tank level  >> return expected consumed fuel
        ## if expected consumed fuel > current tank_level >> empty tank level >> return the current tank level before empty
        return

    # if fuel is not enough, distance based on remaining fuel
    def drive(self, time):
        required_fuel = self.required_fuel(time)
        self.distance = required_fuel * TRAVELLED_DISTANCE_PER_UNIT
        self.consume(time)

    # def drive(self,time):
    #     pass


if __name__ == "__main__":

    #initialize
    car1 = EletricCar("ABC-15",180,52.5)
    car2 = GasolineCar("ACD-123",165,32.3)

    #test
    car1.speed(100)
    car2.speed(150)

    car1.drive(3)
    car2.drive(3)

    print(car1)
    print(car2)