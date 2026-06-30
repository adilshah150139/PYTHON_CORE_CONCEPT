# ============================================================
# 07 - Functions
# ============================================================

# --- Basic function ---
def greet():
    print("Assalamu Alaikum!")

greet()

# --- Function with parameters ---
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Abdullah")
greet_person("Ali")

# --- Function with return value ---
def add(a, b):
    return a + b

result = add(10, 25)
print("Sum:", result)

# --- Default parameter ---
def power(base, exponent=2):
    return base ** exponent

print(power(3))       # 3^2 = 9  (default exponent)
print(power(2, 10))   # 2^10 = 1024

# --- Multiple return values ---
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 1, 9, 2, 7])
print(f"Min: {low}, Max: {high}")

# --- Keyword arguments ---
def describe_student(name, age, major):
    print(f"{name} is {age} years old, studying {major}.")

describe_student(age=19, major="Computer Science", name="Abdullah")

# --- *args: accept any number of arguments ---
def total(*args):
    return sum(args)

print("Total:", total(10, 20, 30, 40))

# --- **kwargs: accept any number of keyword arguments ---
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

show_info(name="Abdullah", city="Xi'an", hobby="Calisthenics")

# --- Docstring: explain what a function does ---
def calculate_gpa(grades):
    """
    Takes a list of grade points and returns the GPA.
    Example: calculate_gpa([4.0, 3.7, 3.3]) → 3.67
    """
    return round(sum(grades) / len(grades), 2)

my_gpa = calculate_gpa([3.7, 3.5, 4.0, 3.3])
print("GPA:", my_gpa)

# --- Recursive function ---
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))   # 120
print("10! =", factorial(10))
