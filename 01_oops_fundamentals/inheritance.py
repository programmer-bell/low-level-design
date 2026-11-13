## Inheritance 
'''
Inheritance allows one class to acquire the properties and methods of another class.
This avoids writing the same code again and again, and makes your codebase much cleaner.

 -  Parent clas contains common share features 
 - Child class inherits everything from the parent
 - Child class aslo add its own new attribues and methods on top
 - Changes made in the parent class automatically reflect in the child class
 - Real life example: animal class has eat() and sleep() that Dog and Cat inherit it, add 
   brak() and meow() on it.

'''

class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        print("Animal Constructor")

    def eat(self):
        print("I am eating")

    @classmethod
    def sleep(self):
        print("I am sleeping")


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed
        print("Dog Constructor")

    def bark(self):
        print("I am barking")

    def display(self):
        print(f"Name is {self.name} Age is {self.age} and Breed {self.breed}")

dog = Dog("Tom", 7, "Haskey")

dog.bark()
dog.eat()
dog.sleep()
dog.display()