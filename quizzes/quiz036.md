## Code

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

![image](https://github.com/user-attachments/assets/abe87347-6a1a-4d7c-8283-794e06bf2d1f)
