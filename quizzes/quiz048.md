## Code
```.py
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def show_books(self):
        if not self.books:
            print("No books in library.")
        else:
            print("Books in library:")
            for book in self.books:
                book.display_info()

# tests
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.show_books()
```
## Proof Code Works
![image](https://github.com/user-attachments/assets/a3a30acf-0359-47c5-a22a-c15a154f0ff9)
## UML Diagram
![image](https://github.com/user-attachments/assets/214c7567-9791-4bbb-95f2-f0eb71039818)
