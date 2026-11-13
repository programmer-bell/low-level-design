class Engine:
    def __init__(self, horsepower: int) -> None:
        self.__horsepower: int = horsepower

    def get_horsepower(self) -> int:
        return self.__horsepower


class Car:
    def __init__(self, model: str, horsepower: int) -> None:
        self.__model: str = model
        # Composition: Engine is created *inside* the Car. 
        # Its lifecycle is managed entirely by the Car container.
        self.__engine: Engine = Engine(horsepower)

    def get_car_details(self) -> str:
        return f"Car Model: {self.__model}, Engine: {self.__engine.get_horsepower()} HP"


# Usage
my_car: Car = Car("Tesla Model S", 670)
print(my_car.get_car_details())

# If my_car is deleted, the Engine instance created inside it goes away too.
del my_car