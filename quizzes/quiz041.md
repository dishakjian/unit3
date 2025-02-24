## Proof Code Works
![image](https://github.com/user-attachments/assets/8240298f-46f1-4338-ad4c-8d60bd174afc)
hashed results
![image](https://github.com/user-attachments/assets/f857e32c-dc1d-46e8-907a-3230840483db)

## Code
```.py
import sqlite3
from kivymd.app import MDApp
from kivy.lang import Builder
import hashlib


def encrypt_password(data):
    return hashlib.sha256(data.encode()).hexdigest()

class DatabaseWorker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()


class Quiz047(MDApp):
    def build(self):
        return
    def update(self):
        try:
            base_salary = int(self.root.ids.base.text)
            ids = ["inhabitant", "income_tax", "pension", "health"]
            total = base_salary
            for id_ in ids:
                value = self.root.ids[id_].text.strip()
                if value.isdigit():
                    amount = (base_salary * int(value)) // 100
                    total -= amount
                    self.root.ids[id_ + "_label"].text = f"{amount} JPY"
                else:
                    self.root.ids[id_ + "_label"].text = " JPY"

            self.root.ids.salary_label.text = f"Net Salary: {total} JPY"

            # Generate the hash
            for_hash = f"base{base_salary}," + ",".join(
                [f"{id_}{self.root.ids[id_].text}" for id_ in ids]
            ) + f",total{total}"
            hashed_value = encrypt_password(for_hash)
            self.root.ids.hash.text = hashed_value[-50:]

        except ValueError:
            self.root.ids.salary_label.text = "Invalid Input"

    def save(self):
        try:
            base_salary = int(self.root.ids.base.text)
            ids = ["inhabitant", "income_tax", "pension", "health"]
            deductions = {id_: int(self.root.ids[id_].text) if self.root.ids[id_].text.isdigit() else 0 for id_ in ids}
            total = base_salary - sum((base_salary * deductions[id_]) // 100 for id_ in ids)


            for_hash = f"base{base_salary}," + ",".join(
                [f"{id_}{deductions[id_]}" for id_ in ids]
            ) + f",total{total}"
            hashed_value = encrypt_password(for_hash)

            query = """INSERT INTO payments (base, inhabitant, income_tax, pension, health, total, hash)
                       VALUES (?, ?, ?, ?, ?, ?, ?)"""
            db = DatabaseWorker("payments.db")
            db.run_save(query, (base_salary, deductions["inhabitant"], deductions["income_tax"],
                                deductions["pension"], deductions["health"], total, hashed_value))
            db.close()
            self.root.ids.hash.text = f"Payment saved"

        except ValueError:
            self.root.ids.salary_label.text = "Invalid Input"

    def clear(self):
        for label in ["base", "inhabitant", "income_tax", "pension", "health"]:
            self.root.ids[label].text = ""
            self.root.ids[label + "_label"].text = " JPY"
        self.root.ids.salary_label.text = "Net Salary: JPY"
        self.root.ids.hash.text = "----"

if __name__ == "__main__":
    db = DatabaseWorker("payments.db")
    db.run_save("""
    CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        base INTEGER,
        inhabitant INTEGER,
        income_tax INTEGER,
        pension INTEGER,
        health INTEGER,
        total INTEGER,
        hash TEXT
    )
    """)
    db.close()

    Quiz047().run()
```
```.kv
MDScreen:
    id:bck
    size: 200, 500

    MDBoxLayout:
        id: bck
        size_hint: .8,.9
        md_bg_color: "#F2F2F2"
        orientation: "vertical"
        pos_hint: {"center_x":.5, "center_y":.5}
        spacing: dp(10)

        MDLabel:
            text:"Compensation Calculator"
            halign: "center"
            font_style:"H4"
            color: "#222222"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)

            MDIcon:
                icon: "plus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
            MDLabel:
                text:"Base Salary"
                size_hint_x: .4
            MDTextField:
                id:base
                mode: "rectangle"
                input_filter:"int"
                text_color_normal: "#222222"
                line_color_normal: "#222222"
                hint_text: "Base Salary"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    root.ids.base_label.text = f"{self.text} JPY"
                    app.update()
            MDLabel:
                id: base_label
                text:" JPY"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)


            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text:"Health"
                size_hint_x: .4
                color: "#6a040f"
            MDTextField:
                id:health
                mode: "rectangle"
                input_filter:"int"
                hint_text: "% Health"
                pos_hint: {"center_x": .5, "center_y": .5}
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: health_label
                text:" JPY"
                color: "#9d0208"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)


            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text: "Pension"
                size_hint_x: .4
                color: "#9d0208"
            MDTextField:
                id:pension
                mode: "rectangle"
                input_filter:"int"
                hint_text: "% Pension"
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: pension_label
                text:" JPY"
                color: "#9d0208"


        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)

            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text:"Income Tax"
                size_hint_x: .4
                color: "#9d0208"
            MDTextField:
                id:income_tax
                mode: "rectangle"
                input_filter:"int"
                hint_text: "% Income"
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: income_tax_label
                text:" JPY"
                color: "#9d0208"

        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)


            MDIcon:
                icon: "minus-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#9d0208"
            MDLabel:
                text:"Inhabitant Tax"
                size_hint_x: .4
                color: "#9d0208"
            MDTextField:
                id:inhabitant
                mode: "rectangle"
                input_filter:"int"
                hint_text: "%  Income"
                text_color_normal: "#9d0208"
                line_color_normal: "#9d0208"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_text:
                    self.text = str(max(0, min(100, int(self.text or 0))))
                    app.update()
            MDLabel:
                id: inhabitant_label
                text:" JPY"
                color: "#9d0208"


        MDBoxLayout:
            size_hint_x: .8
            height: dp(46)
            valign: "center"
            md_bg_color: "#22223b"
            pos_hint: {"center_x":.5, "center_y":.5}
            spacing: dp(10)

            MDLabel:
                size_hint_x: .5
            MDIcon:
                icon: "calculator"
                pos_hint: {"center_x": .5, "center_y": .5}
                color: "#F2F2F2"
            MDLabel:
                text:"Net Salary"
                size_hint_x: .4
                color: "#F2F2F2"
            MDLabel:
                id: salary_label
                text:" JPY"
                color: "#F2F2F2"
            MDFloatingActionButton:
                icon:"content-save-plus"
                md_bg_color:"#ffc300"
                icon_color:"#222222"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press:
                    app.save()

            MDFloatingActionButton:
                icon:"autorenew"
                md_bg_color:"#2a9d8f"
                icon_color:"#222222"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press:
                    app.clear()

        MDBoxLayout:
            size_hint: .8, .2
            valign: "center"
            md_bg_color: "#FFFFFF"
            pos_hint: {"center_x":.5, "center_y":.5}

            MDLabel:
                id: hash
                halign: "center"
                text: "----"
                font_style: "Caption"
```


