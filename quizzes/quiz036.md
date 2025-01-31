![image](https://github.com/user-attachments/assets/2fc0da1d-5375-43bd-ac4a-06222f689e52)## Code

```.py

from kivymd.app import MDApp

class change(MDApp):
    def build(self):
        return

    def change_label(self):
        button = self.root.ids.button
        if button.md_bg_color == [1, 1, 1, 1]:
            button.md_bg_color = [0, 0, 0, 1]
            button.text_color = [1, 1, 1, 1]
        else:
            button.md_bg_color = [1, 1, 1, 1]
            button.text_color = [0, 0, 0, 1]
        print("hello, the button was pressed")

test = change()
test.run()

```

## Proof Code Works
![Screenshot 2025-01-30 085255](https://github.com/user-attachments/assets/c2416be3-9b3f-4b26-982d-abe860111e9b)
![Screenshot 2025-01-30 085250](https://github.com/user-attachments/assets/7dc848f7-5ed7-46e2-b0a9-53fcb69267d8)
^ Further clarification and tasks/additions were given after initial code


## Diagram

![image](https://github.com/user-attachments/assets/5f134b2d-3def-43b1-b81c-4199890e6bae)
