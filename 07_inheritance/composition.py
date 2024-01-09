from math import pi


class Tyre:

    def __init__(self, material: str, radio: float):
        self.material = material
        self.radio = radio

    def circumference(self) -> float:
        return 2 * pi * (self.radio ** 2)


class Car:

    def __init__(self, brand: str, cv: int, tyre: Tyre):
        self.brand = brand
        self.cv = cv
        self.tyre = tyre

    def drive(self):
        print(f'{self} is driving')


if __name__ == '__main__':

    car1: Car = Car('Audi A3', 149, Tyre('Gum', 1.02))
    print(car1.tyre.circumference())
