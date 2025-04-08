from car import Car


class Tank(Car):
    def __init__(self, weight, length, max_speed, projectile_caliber, shots_per_minute, crew_size):
        super().__init__(weight, length, max_speed)
        self.projectile_caliber = projectile_caliber
        self.shots_per_minute = shots_per_minute
        self.crew_size = crew_size

    def drive(self):
        print(f"Driving {self.__class__.__name__} with "
              f"Caliber: {self.projectile_caliber}mm, RPM: {self.shots_per_minute}, "
              f"Crew: {self.crew_size}, Max Speed: {self.max_speed}km/h")


# Tanks
class Tiger(Tank):
    def __init__(self):
        super().__init__(weight=45000, length=6.1, max_speed=45,
                         projectile_caliber=88, shots_per_minute=9, crew_size=3)


class Abrams(Tank):
    def __init__(self):
        super().__init__(weight=50000, length=7.2, max_speed=50,
                         projectile_caliber=120, shots_per_minute=8, crew_size=4)


class Merkava(Tank):
    def __init__(self):
        super().__init__(weight=55000, length=7.5, max_speed=60,
                         projectile_caliber=120, shots_per_minute=9, crew_size=4)