import os
with open("notes.text", 'w') as file:
    file.write("1. This is python file-handling practice.\n")
    file.write("2. Today I'm so happy that I gonna learn, python file management.\n")
    file.write("3. I will be happy when i get internship.")

with open("notes.text", 'r') as file:
    content = file.read()
    print("*** File Content ***")
    print(content)

print("*************--#--***************")

with open("notes.text", 'r') as file:
    print("print ---Line by line")
    for line in file:
        print(line.strip())

# ovid overwriting:
with open ("notes.text", 'a') as file:
    file.write("\n4. Inshallah in next month, I will apply for internship.")

with open("notes.text", 'r') as file:
    print("4 LINES FILE:")
    for line in file:
        print(line.strip())
    
# Check file, is it exist or not:
file_name = "notes.text"
print("File checking...")
if os.path.exists(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    print("YOUR file read successfully. Thank you!")
else:
    print(f"{file_name}, doesn't exist. Make sure that your path must correct")

loads = [line.strip() line in file.readlines]