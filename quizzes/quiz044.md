## Paper Solution

![photo_2025-02-25_07-22-16](https://github.com/user-attachments/assets/affecb8a-c997-4bc0-8cfd-23ef16876756)


## Code
```.py
class RainDrops:
    def pour(self, n: int) -> str:
        result = ""
        if n % 3 == 0:
            result += "Pling"
        if n % 5 == 0:
            result += "Plang"
        if n % 7 == 0:
            result += "Plong"
        return result if result else str(n)

raindrops = RainDrops()
print(raindrops.pour(28))
print(raindrops.pour(30))
print(raindrops.pour(34))  

```
## Proof Code Works
![image](https://github.com/user-attachments/assets/80b4262b-33c6-48a2-9310-488f93535bdf)

## UML Diagram

![image](https://github.com/user-attachments/assets/5eecbc81-3100-4e67-a76d-b6e8041e2747)
