# ============================================================
# 08 - File Handling
# ============================================================
# Python can read from and write to files on your computer.

import os

# --- Write to a file ---
with open("notes.txt", "w") as file:
    file.write("Python File Handling Practice\n")
    file.write("Line 2: Learning to write files\n")
    file.write("Line 3: This is beginner level\n")

print("File written successfully!")

# --- Read entire file ---
with open("notes.txt", "r") as file:
    content = file.read()
    print("\n--- File Content ---")
    print(content)

# --- Read line by line ---
with open("notes.txt", "r") as file:
    print("--- Line by Line ---")
    for line in file:
        print(line.strip())   # .strip() removes the \n at end

# --- Append to file (doesn't overwrite) ---
with open("notes.txt", "a") as file:
    file.write("Line 4: Added with append mode\n")

# --- Read all lines into a list ---
with open("notes.txt", "r") as file:
    lines = file.readlines()
    print(f"\nTotal lines: {len(lines)}")
    print("First line:", lines[0].strip())

# --- Check if file exists before reading ---
filename = "maybe_exists.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f.read())
else:
    print(f"\n'{filename}' does not exist — safe check passed!")

# --- Write a list of items to a file ---
subjects = ["Calculus", "Linear Algebra", "Physics", "Discrete Math"]
with open("subjects.txt", "w") as file:
    for subject in subjects:
        file.write(subject + "\n")

# --- Read it back ---
with open("subjects.txt", "r") as file:
    loaded = [line.strip() for line in file.readlines()]
    print("\nLoaded subjects:", loaded)

# --- Clean up created files (optional) ---
# os.remove("notes.txt")
# os.remove("subjects.txt")
print("\nFile handling complete!")
