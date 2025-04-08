from car import Car


class Cargo(Car):
    def __init__(self, weight, length, max_speed, tonnage, tank_volume, axles_amount):
        super().__init__(weight, length, max_speed)
        self.tonnage = tonnage
        self.tank_volume = tank_volume
        self.axles_amount = axles_amount

    def drive(self):
        print(f"Driving {self.__class__.__name__} with "
              f"Tonnage: {self.tonnage}t, Tank Volume: {self.tank_volume}L, "
              f"Axles: {self.axles_amount}, Max Speed: {self.max_speed}km/h")


# Cargo
class Volvo(Cargo):
    def __init__(self):
        super().__init__(weight=8000, length=7.5, max_speed=120,
                         tonnage=15, tank_volume=500, axles_amount=4)


class Man(Cargo):
    def __init__(self):
        super().__init__(weight=7700, length=7.2, max_speed=115,
                         tonnage=16, tank_volume=480, axles_amount=5)


class Scania(Cargo):
    def __init__(self):
        super().__init__(weight=8200, length=7.8, max_speed=125,
                         tonnage=18, tank_volume=500, axles_amount=5)