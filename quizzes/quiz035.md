## Code

```.py
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age


class Student(Person):
    def __init__(self, name: str, age: int, grade: int):
        super().__init__(name, age)
        self.grade = grade

    def get_grade(self) -> int:
        return self.grade


# Test cases
# Person instance
test1 = Person(name="Smith", age=20)
print(f"Name: {test1.get_name()}, Age: {test1.get_age()}")

# Student instance
test2 = Student(name="Bob", age=10, grade=7)
print(f"Name: {test2.get_name()}, Age: {test2.get_age()}, Grade: {test2.get_grade()}")

```

## Proof Code Works

![image](https://github.com/user-attachments/assets/76bb12a6-e992-4799-9dbe-9af0cd59f3a5)


## Diagram

![image](https://github.com/user-attachments/assets/ee3e7485-a4da-4ffa-8c63-40cb2b07b83d)

