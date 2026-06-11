# ============================================================
# 05 - Conditionals (if / elif / else)
# ============================================================

score = 74

# --- Basic if/elif/else ---
if score >= 90:
    print("Grade: A — Excellent!")
elif score >= 80:
    print("Grade: B — Good job")
elif score >= 70:
    print("Grade: C — Acceptable")
elif score >= 55:
    print("Grade: D — Needs work")
else:
    print("Grade: F — Study harder!")

# --- Comparison operators ---
x = 10
y = 20
print(x == y)   # It will give "false" because not equale;
print(x != y)  
print(x < y)    
print(x >= 10)  

# --- Logical operators: and, or, not ---
age = 21
has_id = True 

if age >= 18 and has_id:
    print("Access granted")

temperature = 35
if temperature > 40 or temperature < 0:
    print("weather is so hot")
else:
    print("Weather is okay")

is_raining = False
if not is_raining:
    print("No rain, good to go outside")

# --- Nested if ---
marks = 88
attendance = 75

if attendance >= 70:
    if marks >= 85:
        print("excelent score with good attendance!")
    else:
        print("Good attendance but marks could improve")
else:
    print(f"your attendance is: {attendance}, U can't give exam")



# --- One-liner (ternary or composed form syntax) ---

status = "pass" if score >= 50 else "fail"
print("status:", status)
# --- in operator ---
allowed_users = ["admin", "professor", "ta"]
current_user = "admin"
if current_user in allowed_users:
    print(f"{current_user} has system access")
