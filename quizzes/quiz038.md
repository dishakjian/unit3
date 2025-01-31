## Code

```.py
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class MysteryPageA(MDScreen):
    pass

class MysteryPageB(MDScreen):
    pass

class mystery(MDApp):
    def build(self):
        return

t = mystery()
t.run()
```
KIVY
```.kv
ScreenManager:
    id: screen_manager
    MysteryPageA:
        name: "MysteryPageA"
    MysteryPageB:
        name: "MysteryPageB"

<MysteryPageA>:
    MDFloatLayout:
        MDLabel:
            text: "This is Mystery Page A"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
        MDRaisedButton:
            text: "Go to Page B"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            on_release: app.root.current = "MysteryPageB"

<MysteryPageB>:
    MDFloatLayout:
        MDLabel:
            text: "This is Mystery Page B"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
        MDRaisedButton:
            text: "Go to Page A"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            on_release: app.root.current = "MysteryPageA"
```


## Proof Code Works
![Screenshot 2025-01-31 094421](https://github.com/user-attachments/assets/0acac101-3b98-4cd6-befa-3e0d22e2d028)
![Screenshot 2025-01-31 094427](https://github.com/user-attachments/assets/6ade9f67-8dd0-4a2c-808e-0e93a9474556)


## UML Diagram
![image](https://github.com/user-attachments/assets/ca4f6581-3cca-4313-97a7-72eb6393a401)
