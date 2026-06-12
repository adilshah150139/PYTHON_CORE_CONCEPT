# ============================================================
# 04 - Dictionaries and Sets
# ============================================================

# --- DICTIONARY: key → value pairs ---
student = {
    "name": "Adil shah",
    "age": 21,
    "university": "Xidian University",
    "major": "Computer Science",
    "gpa": 3.5,
    "nationality": "Pakistan"
}

# Access a value by key
print("Name:", student["name"])
print("GPA:", student["gpa"])

# Safer access with .get() — no crash if key missing
# means if the key is exist then it will otherwise it will run your comment
print("City:", student.get("city", "Not specified"))
print("Language:", student.get("language", "Sorry, you didn't set your Language yet!"))

# --- Add or update ---
student["city"] = "Xi'an"
student["gpa"] = 3.7
print("\nUpdated student:", student)

# --- Delete a key ---
del student["city"]
print("After deleting city:", student)

# --- Loop through (for loop) ---
print("\n Student all info:")
for key, value in student.items():    # .items() returns a collection of (key, value) tuples — your loop just unpacks them automatically with key, value.
    print(f"  {key}: {value}")

# --- Just keys or just values ---
print("************* Conversion of dict_keys ot list *************")
print("\nKeys:", list(student.keys()))      # converts dict_keys to list for printin
print("Values:", list(student.values()))

# --- Check if key exists ---
print("\n'name' in student:", "name" in student)
print("'phone' in student:", "phone" in student)

# --- Nested dictionary ---
grades = {
    "Calculus": {"midterm": 78, "final": 85},
    "Physics":  {"midterm": 82, "final": 90},
}
print("\nCalculus final:", grades["Calculus"]["final"])

# ============================================================
# SET: unordered, no duplicates
# ============================================================
languages = {"Python", "C", "Java", "Python", "C"}
print("\nLanguages set:", languages)   # Python & C appear once only

languages.add("JavaScript")
print("After add:", languages)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a | set_b)           # '|' This works as Uninion'
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)


print("*************** The End Of Python Dictionary ***************************")