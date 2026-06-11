# ============================================================
# 01 - Variables and Data Types
# ============================================================


# --- Numbers ---
age = 19
gpa = 3.7
print("Age:", age)
print("GPA:", gpa)
print("Type of age:", type(age))       # int
print("Type of gpa:", type(gpa))       # float

# --- Text (String) ---
name = "ADIL SHAH"
university = "Xidian University"
future_plan = "My future is to go to Germany"
print("Name:", name)
print("University:", university)
print("Goal:", future_plan)

# --- Boolean (True / False) ---
is_student = True
has_passed = False
print("Is student?", is_student)
print("Has passed?", has_passed)

# --- Checking types ---
print(type(name))         # <class 'str'>
print(type(is_student))   # <class 'bool'>

# --- Basic arithmetic ---
x = 10
y = 3
print("Add:", x + y)
print("Subtract:", x - y)
print("Multiply:", x * y)
print("Divide:", x / y)       # always gives float
print("Floor divide:", x // y) # removes decimal
print("Remainder:", x % y)
print("Power:", x ** y)

# --- User input ---
# Uncomment the lines below to try interactive input:
# user_name = input("What is your name? ")
# print("Hello,", user_name)
