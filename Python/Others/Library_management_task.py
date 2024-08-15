
#* Create a library management --> types of books, detail of books
#* inheritance --> different categories, calculate the return fee for each book type
# late fee for "the name":"the fee"
#*! Main class
class Book:
    def __init__(self, title, author, days_late):
        self.title = title
        self.author = author
        self.days_late = days_late
    def calculate_late_fee(self):
        print("Calculating late fee...")

#*! Inheritance process
class Fiction(Book):
    def __init__(self, title, author, days_late, genre):
        super().__init__(title, author, days_late)
        self.genre = genre
    def calculate_late_fee(self):
        return print(f"Late fee for '{self.title}' : ${self.days_late * 1.5}")

class NonFiction(Book):
    def __init__(self, title, author, days_late, subject):
        super().__init__(title, author, days_late)
        self.subject = subject
    def calculate_late_fee(self):
        return print(f"Late fee for '{self.title}' : ${self.days_late * 2}")

class Magazine(Book):
    def __init__(self, title, author, days_late, issue_number):
        super().__init__(title, author, days_late)
        self.issue_number = issue_number
    def calculate_late_fee(self):
        return print(f"Late fee for '{self.title}' : ${self.days_late * 1}")
    
#*! Instance creation
main = Book("pass", "pass", 0)
obj1 = Fiction("1984", "pass", 3, "fiction")
obj2 = NonFiction("Sapiens", "pass", 4, "history")
obj3 = Magazine("National Geographic", "pass", 5, 1234567890)

#*! Final output
main.calculate_late_fee()
obj1.calculate_late_fee()
obj2.calculate_late_fee()
obj3.calculate_late_fee()

