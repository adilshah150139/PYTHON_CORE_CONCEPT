# ============================================================
# 02 - Strings
# ============================================================

name = "Adil Shah"
city = "Peshawar"

# --- Length ---
print("Length:", len(name))     # Length: 9

 # --- Upper / Lower ---
print(name.upper())
print(name.lower())

  # --- Slicing: string[start:end] ---
print(name[0])        # First character: A
print(name[-1])       # Last character: h
print(name[0:3])      # First 4 letters: 

# --- Check if something is inside ---
sentence = "Python is fun and Python is powerful"
print("Python" in sentence)   # True
print("Java" in sentence)     # False

# --- Replace ---
new_sentence = sentence.replace("Python", "Programming")
print(new_sentence)

# --- Split into a list ---
words = sentence.split(" ")
print(words)

 # --- Strip whitespace --- (mean it will remove the white space from both side)
messy = "   hello world   "
print(messy.strip())

# --- f-strings: 
age = 21
message = f"My name is {name} and I am {age} years old."
print(message)

# --- Count occurrences ---
print(sentence.count("Python"))  # 2

# --- Starts / Ends with ---
print(name.startswith("Ad"))   # True
print(name.endswith("il"))    # True
