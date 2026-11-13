class Teacher:
    def __init__(self, name: str) -> None:
        self.__name: str = name # Private

    def get_name(self) -> None:
        return self.__name
    
    def teach(self, student: "Student") -> None:
        print(f"{self.__name} is teaching {student.get_name()}")

class Student:
    def __init__(self, name: str) -> None:
        self.__name: str = name # Private

    def get_name(self) -> None:
        return self.__name

teacher1 = Teacher("Sukanta Prasad")
student1 = Student("Subham Modak")

teacher1.teach(student1)