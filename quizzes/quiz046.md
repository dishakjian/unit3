## Code
```.py
class Citizen:
    def __init__(self, name: str, city: str, status: str):
        self.name = name
        self.city = city
        self.status = status

    def getName(self) -> str:
        return self.name

    def getCity(self) -> str:
        return self.city

    def getStatus(self) -> str:
        return self.status


class Employee(Citizen):
    def __init__(self, name: str, city: str, status: str, annualSalary: float):
        super().__init__(name, city, status)
        self.annualSalary = annualSalary

    def getAnnualSalary(self) -> float:
        return self.annualSalary


class PartTimeEmployee(Employee):
    def __init__(self, name: str, city: str, status: str, annualSalary: float, fraction: float, isUnionMember: bool):
        super().__init__(name, city, status, annualSalary)
        self.fraction = fraction
        self._isUnionMember = isUnionMember  # Use an underscore to avoid conflict

    def getFraction(self) -> float:
        return self.fraction

    def getIsUnionMember(self) -> bool:  # Renamed method to avoid conflict
        return self._isUnionMember


# Examples
citizen = Citizen("John Doe", "New York", "Single")
print(citizen.getName(), citizen.getCity(), citizen.getStatus())

employee = Employee("Alice Smith", "Los Angeles", "Married", 60000)
print(employee.getName(), employee.getAnnualSalary())

part_time_emp = PartTimeEmployee("Bob Brown", "Chicago", "Single", 40000, 0.5, True)
print(part_time_emp.getName(), part_time_emp.getFraction(), part_time_emp.getIsUnionMember())
```
## Proof Code Works
![image](https://github.com/user-attachments/assets/cd43b456-59ac-4ef1-bef8-e838e4d7dc1c)

## UML Diagram
given
![image](https://github.com/user-attachments/assets/42b226aa-2546-48e4-8a74-2fba5d0269e2)
