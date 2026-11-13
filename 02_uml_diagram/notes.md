## 1. Association (`uses-a` relationship)

**Concept:** 
Association represents a relationship where two independent classes interact with each other, but neither owns the other. Both `Teacher` and `Student` have their own independent lifecycles—if the `Teacher` object is deleted, the `Student` object still exists (and vice versa).

In this code, `Teacher` temporarily interacts with `Student` by accepting it as a method parameter (`teach(student)`), rather than storing it as an instance attribute.

### UML Class Diagram (Text Format)

```text
+-----------------------------------+               +-----------------------------------+
|              Teacher              |               |              Student              |
+-----------------------------------+               +-----------------------------------+
| - __name: str                     |               | - __name: str                     |
+-----------------------------------+               +-----------------------------------+
| + __init__(name: str) -> None     |               | + __init__(name: str) -> None     |
| + get_name() -> str               |  1..*   1..*  | + get_name() -> str               |
| + teach(student: Student) -> None | ------------> |                                   |
+-----------------------------------+   teaches     +-----------------------------------+
```


## 2. Aggregation (`has-a` relationship with weak ownership)

**Concept:** 
Aggregation represents a specialized `has-a` relationship where one class (the whole) contains references to other classes (the parts), but both entities have **independent lifecycles**. 

In this code, a `Department` holds a list of `Student` objects (`self.__students`). However, if the `Department` object is deleted (`del cs_dept`), the `Student` objects (`s1`, `s2`, `s3`) continue to exist independently in memory.

### UML Class Diagram (Text Format)

```text
+-----------------------------------+               +-----------------------------------+
|            Department             |               |              Student              |
+-----------------------------------+               +-----------------------------------+
| - __dept_name: str                |               | - __name: str                     |
| - __students: List[Student]       |               | - __roll_no: int                  |
+-----------------------------------+               +-----------------------------------+
| + __init__(dept_name: str) -> None|    1     0..* | + __init__(name: str, roll) -> None|
| + add_student(student: Student)   | <>----------> | + get_name() -> str               |
| + show_students() -> None         |   contains    | + get_roll_no() -> int            |
+-----------------------------------+               +-----------------------------------+
```


## 3. Composition (`has-a` relationship with strong ownership)

**Concept:** 
Composition is a restricted form of aggregation representing **strong ownership** and strict lifecycle dependency (a "part-whole" relationship). In composition, the component parts cannot exist independently of the container object. 

If the container object (the whole) is destroyed, its constituent parts are destroyed along with it. 

In this code, a `Car` *owns* an `Engine`. The `Engine` is instantiated directly inside the `Car`'s constructor (`__init__`). If the `Car` object is deleted (`del my_car`), the `Engine` object ceases to exist with it.

### UML Class Diagram (Text Format)

```text
+-----------------------------------+               +-----------------------------------+
|                Car                |               |              Engine               |
+-----------------------------------+               +-----------------------------------+
| - __model: str                    |               | - __horsepower: int               |
| - __engine: Engine                |               +-----------------------------------+
+-----------------------------------+               | + __init__(horsepower: int) -> None|
| + __init__(model: str, hp: int)   |  1      1     | + get_horsepower() -> str         |
| + get_car_details() -> str        | ♦---------->  |                                   |
+-----------------------------------+   owns        +-----------------------------------+
```


## 4. Inheritance (`is-a` relationship)

**Concept:** 
Inheritance is an Object-Oriented Programming pillar that allows a new class (**Child/Subclass**) to adopt the attributes and methods of an existing class (**Parent/Superclass**). It promotes code reusability and establishes a hierarchical `is-a` relationship (e.g., a `Student` *is-a* `Person`).

In this code, `Student` inherits from `Person`. It uses `super().__init__()` to reuse the parent's initialization logic while adding its own specialized attributes (`__roll_no`) and behaviors.

### UML Class Diagram (Text Format)

```text
+-----------------------------------+
|              Person               |
+-----------------------------------+
| - __name: str                     |
| - __age: int                      |
+-----------------------------------+
| + __init__(name: str, age: int)   |
| + get_name() -> str               |
| + get_age() -> int                |
+-----------------------------------+
                  ▲
                  │  Inheritance (Generalization)
                  │
+-----------------------------------+
|              Student              |
+-----------------------------------+
| - __roll_no: int                  |
+-----------------------------------+
| + __init__(name, age, roll_no)    |
| + get_roll_no() -> int            |
| + get_student_details() -> str    |
+-----------------------------------+
```

## 5. Dependency (`uses-a` / transient relationship)

**Concept:** 
Dependency is a weaker "uses-a" relationship where one class (the independent class) is used temporarily by another class (the dependent class). Typically, the dependent class receives the independent object as a method argument, creates it locally inside a method, or calls a static method, **without storing it as an instance attribute**.

A change in the independent class (e.g., `Car`) may occasionally affect the dependent class (`Driver`), but there is no persistent structural ownership or association.

### UML Class Diagram (Text Format)

```text
+-----------------------------------+               +-----------------------------------+
|              Driver               |               |                Car                |
+-----------------------------------+               +-----------------------------------+
| - __name: str                     |               | - __brand: str                    |
+-----------------------------------+               +-----------------------------------+
| + __init__(name: str) -> None     |  . . . . . .> | + __init__(brand: str) -> None    |
| + drive(car: Car) -> None         |   depends-on  | + start_engine() -> str           |
+-----------------------------------+               +-----------------------------------+