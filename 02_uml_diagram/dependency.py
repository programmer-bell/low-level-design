class Car:
    def __init__(self, brand: str) -> None:
        self.__brand: str = brand

    def start_engine(self) -> str:
        return f"The {self.__brand} engine roars to life!"


class Driver:
    def __init__(self, name: str) -> None:
        self.__name: str = name

    # Dependency: Car is passed as a method parameter transiently. 
    # Driver does not store 'car' as a permanent instance attribute (self.__car).
    def drive(self, car: Car) -> None:
        print(f"{self.__name} gets in the car. {car.start_engine()}")


# Usage
my_car: Car = Car("BMW")
driver: Driver = Driver("Alice")

# Driver depends on Car temporarily during the method call
driver.drive(my_car)