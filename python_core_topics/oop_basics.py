# ============================================================
# 09 - Object-Oriented Programming (OOP) Basics
# ============================================================
# A class is like a blueprint. An object is something built from that blueprint.

# --- Basic Class ---
class Student:
    # __init__ runs when you create a new object
    def __init__(self, name, age, major):
        # attributes
        self.name = name       # INSTANCE variable - unique
        self.age = age
        self.major = major
        self.grades = []

    # Method: a function inside a class
    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, studying {self.major}.")

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_gpa(self):
        if not self.grades:
            return 0
        return round(sum(self.grades) / len(self.grades), 2)

    # __str__: what gets printed when you print the object 
    def __str__(self):      # it's a special or 'dunder' method in Python that controls how an object is represented as a string.
        return f"Student({self.name}, GPA: {self.get_gpa()})"


# --- Creating objects ---
s1 = Student("Abdullah", 19, "Computer Science")
s2 = Student("Ali", 20, "Electrical Engineering")

s1.introduce()
s2.introduce()

s1.add_grade(3.7)
s1.add_grade(3.5)
s1.add_grade(4.0)
print("Abdullah's GPA:", s1.get_gpa())
print(s1)   # calls __str__

# --- Inheritance: a child class inherits from parent ---
class GraduateStudent(Student):
    def __init__(self, name, age, major, thesis_topic):
        super().__init__(name, age, major)   # call parent __init__
        self.thesis_topic = thesis_topic

    def introduce(self):
        super().introduce()
        print(f"  Thesis: {self.thesis_topic}")


grad = GraduateStudent("Dr. Khalid", 26, "AI", "Deep Learning for Medical Imaging")
grad.introduce()

# --- Class variable (shared by all objects) ---
class Counter:
    count = 0   # class variable, directly defined - shared

    def __init__(self):
        Counter.count += 1 

    @classmethod
    def get_count(cls):
        return cls.count

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(f"\nTotal Counter objects created: {Counter.get_count()}")



# --- Simple Bank Account example ---
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def __str__(self):
        return f"{self.owner}'s account — Balance: {self.balance}"


account = BankAccount("Abdullah", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
print(account)
