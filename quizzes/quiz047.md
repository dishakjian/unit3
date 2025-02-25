## Paper Solution

![photo_2025-02-25_13-07-37](https://github.com/user-attachments/assets/b0b59663-0153-4175-9742-bed47d13c3cb)


## Code
```.py
class CalorieCount:
    def __init__(self, daily_limit: int):
        self.daily_limit = daily_limit
        self.daily_intake = 0
        self.protein = 0
        self.carbs = 0
        self.fat = 0

    def addMeal(self, cal: int, pro: int, car: int, fat: int):
        self.daily_intake += cal
        self.protein += pro
        self.carbs += car
        self.fat += fat

    def getProteinPercentage(self) -> float:
        if self.daily_intake == 0:
            return 0.0
        return (4 * self.protein) / self.daily_intake

    def onTrack(self) -> bool:
        return self.daily_intake <= self.daily_limit


# tests
sunday = CalorieCount(1500)

sunday.addMeal(716, 38, 38, 45)
sunday.addMeal(230, 16, 8, 16)
sunday.addMeal(568, 38, 50, 24)

print(sunday.onTrack())
print(sunday.getProteinPercentage())
```
## Proof Code Works
![image](https://github.com/user-attachments/assets/c73771c9-f44b-47be-be68-d1c53665b195)
## UML Diagram 
![image](https://github.com/user-attachments/assets/e418656c-5e47-4292-9ad0-10d28ae22583)
