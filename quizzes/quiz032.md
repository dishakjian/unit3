## Paper Solution

![photo_2025-01-30_08-34-43](https://github.com/user-attachments/assets/ffa69d94-ed8c-4916-820f-b331f2aedb74)

## Code
```.py
email_list = []

class HResources:
    def __init__(self, name, email, nationality, job):
        self.fullname = name
        self.nationality = nationality
        self.job = job
        self.email = email


    def get_email(self):
        if " " in self.fullname:
            fname, lname = self.fullname.split(" ", 1)
        else:
            fname, lname = self.fullname, "unknown" 

        new_email = f'{fname}.{lname}@uwcisak.jp'.lower()

        if new_email in email_list:
            print("This email address is already in use.")
            return None
        else:
            email_list.append(new_email)
            self.email = new_email
            return self.email

    def greet(self):
        print(f"Welcome to UWC ISAK Japan!"
              f"\nName: {self.fullname}"
              f"\nNationality: {self.nationality}"
              f"\nEmail: {self.email if self.email else 'Not Assigned'}"
              f"\nOccupation: {self.job}")

# Test case
test1 = HResources(name="Bob Smith", email=None, nationality="Egyptian", job="ESS Teacher")
test1.greet()

```

## Proof Code Works

![image](https://github.com/user-attachments/assets/8ddd40cc-c7cc-41f7-b66d-9c830a449801)

