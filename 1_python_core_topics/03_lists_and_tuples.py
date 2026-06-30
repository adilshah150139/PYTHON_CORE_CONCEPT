# ============================================================
# 03 - Lists and Tuples
# ============================================================

# --- LIST: ordered, changeable ---
subjects = ["Calculus", "Linear Algebra", "Physics", "Discrete Math", "Chinese"]

# printing syntax by syntax
print("Subjects:", subjects)
print("First:", subjects[0])              # print 1st element of list
print("Last:", subjects[-1])              # print last element of list
print("Total subjects:", len(subjects))   

# Methods:
# --- Add to list (Updating List) ---
subjects.append("English")
print("After append:", subjects)

# --- Insert at a specific position ---
subjects.insert(1, "Programming")         # Insert 'Programming at 2nd position
print("After insert:", subjects)

# --- Remove ---
subjects.remove("English")
print("After remove:", subjects)

# --- Sort ---
subjects.sort()
print("Sorted:", subjects)

# --- Check membership ---
print("Physics" in subjects)     # True

# --- Loop through a list ---
print("\nAll subjects:")
for subject in subjects:
    print(" -", subject)

# --- List slicing ---
first_two = subjects[0:2]
print("\nFirst two:", first_two)

# --- List of numbers ---
scores = [85, 90, 72, 88, 95]
print("\nMax score:", max(scores))
print("Min score:", min(scores))
print("Total:", sum(scores))
print("Average:", sum(scores) / len(scores))

# --- TUPLE: ordered, but CANNOT be changed ---
# TUPLE, are immutable means can't be changed
coordinates = (31.2304, 121.4737)   # Shanghai lat/long
print("\nCoordinates:", coordinates)
print("Latitude:", coordinates[0])

# Tuples are useful when data should NOT change
days_of_week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print("Days:", days_of_week)
print("Type of days_of_week:", type(days_of_week))
