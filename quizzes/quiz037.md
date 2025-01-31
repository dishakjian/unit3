## Code
```.py

from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder

Window.size = (500, 500)  # Set window size properly

KV = '''
Screen:
    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 0.8, 0.8
        pos_hint: {'center_x':.5, 'center_y':.5}
        md_bg_color: 0.2, 0.3, 0.4, 1  # RGBA instead of hex

        MDLabel:
            id: msg
            text: "Player X"
            size_hint: 1, 0.25
            font_size: '24pt'
            halign: 'center'
            theme_text_color: "Primary"

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.25
            PlayButton:
                id: btn00
            PlayButton:
                id: btn01
            PlayButton:
                id: btn02

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.25
            PlayButton:
                id: btn10
            PlayButton:
                id: btn11
            PlayButton:
                id: btn12

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.25
            PlayButton:
                id: btn20
            PlayButton:
                id: btn21
            PlayButton:
                id: btn22

<PlayButton>:
    size_hint: 1, 1
    font_size: '20pt'
    theme_text_color: "Custom"
    text_color: 1, 1, 1, 1
    md_bg_color: 0.5, 0.8, 0.7, 1  # Default button color
    on_press: app.button_pressed(self)
'''

class PlayButton(MDFlatButton):
    pass

class tictactoe(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0
        self.game_over = False

    def build(self):
        return Builder.load_string(KV)

    def button_pressed(self, btn):
        if self.game_over or btn.text != '':
            return  # Prevent moves after a win

        self.count += 1
        if self.root.ids.msg.text == "Player X":
            btn.text = 'X'
            btn.md_bg_color = (0.74, 0, 0, 1)  # Red
            self.root.ids.msg.text = "Player O"
        else:
            btn.text = 'O'
            btn.md_bg_color = (0.93, 0.84, 0.62, 1)  # Light brown
            self.root.ids.msg.text = "Player X"

        if self.won():
            self.root.ids.msg.text = f'Player {btn.text} won!'
            self.game_over = True
        elif self.count == 9:
            self.root.ids.msg.text = 'Tie!'
            self.game_over = True

    def won(self):
        board = [
            [self.root.ids.btn00.text, self.root.ids.btn01.text, self.root.ids.btn02.text],
            [self.root.ids.btn10.text, self.root.ids.btn11.text, self.root.ids.btn12.text],
            [self.root.ids.btn20.text, self.root.ids.btn21.text, self.root.ids.btn22.text]
        ]
        # Check rows, columns, and diagonals
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                return True
            if board[0][i] == board[1][i] == board[2][i] != "":
                return True
        if board[0][0] == board[1][1] == board[2][2] != "" or board[0][2] == board[1][1] == board[2][0] != "":
            return True
        return False


tictactoe().run()


```


## Proof Code Works

![image](https://github.com/user-attachments/assets/a1dbf4db-53ae-4bd8-ba57-39557e6d9ac6)

## Doagram

![image](https://github.com/user-attachments/assets/ba6f224d-83b9-44c9-93b7-71f1d00cd8d6)


