## Paper Solution

![photo_2025-01-30_08-34-43](https://github.com/user-attachments/assets/a7d02317-d0ac-4be8-8634-1b365573d36c)


## Code
```.py
class CompoundInterest:

    def __init__(self, principal: float, rate: float):
        self.principal = principal
        self.rate = rate

    def calculate(self, years: int) -> float:
        return round(self.principal * (1 + self.rate) ** years, 2)

# Test case
TestCase = CompoundInterest(principal=1000, rate=0.35)

print("Compound Interest")
print(f'8 Years: {TestCase.calculate(8)}')
print(f'16 Years: {TestCase.calculate(16)}')

```
## Proof Code Works

![image](https://github.com/user-attachments/assets/1eb3377b-e988-435c-b9fd-9a98566c2c09)
