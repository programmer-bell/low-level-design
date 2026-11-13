## Polymorphism 

'''
Poly means many, morph means forms. Ploymorphism allows the same method name to 
behave differently depending on which object calls it. This makes your code 
highly flexible and extensible.

- Same method name works differntly for different classes
- You dont need to rembember multiple method names for similar actions
- Method overriding: Child class provides its own version of a parent methods

Real life example: A draw() method on Circel draws a circel, on a Rectangle it 
draws a rectangle -- same name, differnt behavior.

'''


class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        print("Animal Constructor")

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")

    def move(self):
        print("I am moving")


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed
        print("Dog Constructor")

    def bark(self):
        print("I am barking")

    def move(self):
        print("I am moving with 4 legs")    

    def display(self):
        print(f"Name is {self.name} Age is {self.age} and Breed {self.breed}")

dog = Dog("Tom", 7, "Haskey")

dog.bark()
dog.eat()
dog.sleep()
dog.display()
dog.move()