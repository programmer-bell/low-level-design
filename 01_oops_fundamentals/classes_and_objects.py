## Definition 
'''
A Class is just a template. It does not hold any real data on it. When you create an 
object from a class, that's when actual data gets stored and actions can be performed.

Class = Blueprint 
Object = Actual instance build from blueprint

 - A class define what attribues(data) and methods(actions) an object will be have.
 - Multiple objects can be created from the same class, each will their own data.

Example: "Car" is a class. Your Honda City and your friend's Swift are two different 
objects.

'''

class Studnet:

    # Attribues
    # name = "" 
    # age = 0
    # gender = ""

    # Constructor 
    def __init__(self, name: str, age: int, gender: str) -> None:
        print("This is constractor")

        # Attributes
        self.name = name
        self.age = age
        self.gender = gender

    # Methods
    # def self_info(self):
    #     self.name = input("Enter your name = ")
    #     self.age = int(input("Enter your age = "))
    #     self.gender = input("Enter your gender = ")

    # def self_info(self, name:str, age:int, gender:str) -> None:
    #     self.name = name
    #     self.age = age
    #     self.gender = gender

    def display(self) -> None:
        print(f"self = {self}")
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

s1 = Studnet("Bell Shifter", 22, "male")
# print(s1)
# print(s1.name)
# print(s1.age)
# print(s1.gender)

print(s1)
# s1.name = "Badhan Sarkar"
# s1.age = 22
# s1.gender = "Male"

# s1.self_info()
# s1.self_info("Bell Shifter", 22, "male")

# print(s1.name)
# print(s1.age)
# print(s1.gender)

s1.display()