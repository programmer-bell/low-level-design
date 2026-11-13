from typing import List

class Student:
    def __init__(self, name: str, roll_no: int) -> None:
        self.__name = name
        self.__roll_no = roll_no

    def get_name(self) -> str:
        return self.__name

    def get_roll_no(self) -> int:
        return self.__roll_no


class Department:
    def __init__(self, dept_name: str) -> None:
        self.__dept_name: str = dept_name
        self.__students: List[Student] = []

    def add_student(self, student: Student) -> None:
        self.__students.append(student)

    def show_students(self) -> None:
        print(f"\nStudents in {self.__dept_name} Department:")
        for student in self.__students:
            print(f" - {student.get_name()} (Roll No: {student.get_roll_no()})")


s1: Student = Student("Alcok", 101)
s2: Student = Student("Somol", 102)
s3: Student = Student("Tao", 103)

cs_dept: Department = Department("Computer Science")      

cs_dept.add_student(s1)
cs_dept.add_student(s2)
cs_dept.add_student(s3)

cs_dept.show_students()

del cs_dept # Even if we delete the departement, students still exist

print(f"\nStudent still exists:{s1.get_name()}")