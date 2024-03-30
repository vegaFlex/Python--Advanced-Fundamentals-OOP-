from project.car import Car


class SportsCar(Car):
    def race(self):
        return "racing..."


# a = SportsCar()
# print(a.race())
# print(a.move())
# print(a.drive())