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


class Cat(Animal):
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color

    def move(self):
        print("I am moving silently")

    def speak(self):
        print("Meow")


class Bird(Animal):
    def __init__(self, name: str, age: int, wing_span: float):
        super().__init__(name, age)
        self.wing_span = wing_span

    def move(self):
        print("I am flying")

    def speak(self):
        print("Chirp")


def make_animal_move(animal: Animal) -> None:
    animal.move()


make_animal_move(dog)
make_animal_move(Cat("Luna", 3, "Black"))
make_animal_move(Bird("Tweety", 1, 12.5))


class Circle:
    def draw(self):
        print("Drawing a circle")


class Rectangle:
    def draw(self):
        print("Drawing a rectangle")


class Triangle:
    def draw(self):
        print("Drawing a triangle")


def draw_shape(shape):
    shape.draw()


draw_shape(Circle())
draw_shape(Rectangle())
draw_shape(Triangle())


class Printer:
    def print_document(self, copies: int = 1) -> None:
        print(f"Printing {copies} copy/copies")


printer = Printer()
printer.print_document()
printer.print_document(3)


animals = [dog, Cat("Luna", 3, "Black"), Bird("Tweety", 1, 12.5)]
for animal in animals:
    animal.move()