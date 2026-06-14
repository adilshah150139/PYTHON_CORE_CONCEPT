# ============================================================
# 06 - Loops
# ============================================================

# --- for loop with range ---
print("Counting 1 to 5:")
for i in range(1, 6):
    print(i)

# --- for loop over a list ---
fruits = ["apple", "banana", "mango", "orange"]
print("\nFruits:")
for fruit in fruits:
    print(" -", fruit)

# --- enumerate: get index AND value ---
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# --- Loop over a string ---
word = "Python"
print("\nLetters in Python:")
for letter in word:
    print(letter, end=" ")
print()  # newline

# --- while loop ---
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Go!")

# --- break: exit the loop early ---
print("\nLooking for mango:")
for fruit in fruits:
    if fruit == "mango":
        print("Found mango! Stopping.")
        break
    print("Not mango:", fruit)

# --- continue: skip current iteration ---
print("\nSkipping banana:")
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# --- Nested loop ---
print("\nMultiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()

# --- List comprehension (compact loop) ---
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
squares = [n ** 2 for n in numbers]
print("\nEven numbers:", evens)
print("Squares:", squares)

# --- while with user-like simulation ---
attempts = 0
password = "xidian2024"
guesses = ["wrong1", "wrong2", "xidian2024"]  # simulating input

for guess in guesses:
    attempts += 1
    if guess == password:
        print(f"\nCorrect password! Took {attempts} attempt(s).")
        break
else:
    print("All attempts failed.")
