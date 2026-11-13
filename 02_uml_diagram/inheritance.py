class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name: str = name
        self.__age: int = age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age


class Student(Person):  # Student inherits from Person (is-a relationship)
    def __init__(self, name: str, age: int, roll_no: int) -> None:
        # Call the parent class constructor to initialize inherited attributes
        super().__init__(name, age)
        self.__roll_no: int = roll_no

    def get_roll_no(self) -> int:
        return self.__roll_no

    def get_student_details(self) -> str:
        # Accessing inherited methods (get_name, get_age) from Person
        return f"Name: {self.get_name()}, Age: {self.get_age()}, Roll No: {self.__roll_no}"


# Usage
student: Student = Student("Rahul Sharma", 20, 105)
print(student.get_student_details())