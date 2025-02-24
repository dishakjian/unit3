## Paper Solution

![photo_2025-02-25_07-20-52](https://github.com/user-attachments/assets/8b4dbc66-9bd2-4ee9-a037-63d528ad4213)


## Code
```.py
class PalNum:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def get_pal_list(self):
        return [num for num in range(self.A, self.B + 1) if str(num) == str(num)[::-1]]

pal1 = PalNum(1, 9)
print(pal1.get_pal_list())

pal2 = PalNum(10, 199)
print(pal2.get_pal_list())

```
## Proof Code Works
![image](https://github.com/user-attachments/assets/ae7cff0c-b7cb-4636-a3a5-ea83389ae31c)
## UML Diagram
![image](https://github.com/user-attachments/assets/74e3273d-567a-4b57-bf4c-d103f2c75910)
