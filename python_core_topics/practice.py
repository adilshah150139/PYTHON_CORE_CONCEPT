class Student:
    def __init__(self, name, age, major ):
        self.name = name
        self.age = age
        self.major = major
        self.grades = []
    
    def introduce(self):
        print(f"Hi! my name is {self.name} and I'm {self.major} student.")

    def get_grade(self, grade_list):
        self.grades.extend(grade_list)

    def get_gpa(self):
        if not self.grades:
            return 0
        return round(sum(self.grades) / len(self.grades), 2)
    
    def __str__(self):
        return f"student {self.name}, GPA: {self.get_gpa()}"

s1 = Student("Adil shah", 22, "computer science")
s2 = Student("ALi ", 23, "Biology")

s1.introduce()
s2.introduce()

s1.get_grade([3.4, 1.3, 3.4, 2.8])

print("Adil's GPA: ", s1.get_gpa())
print(s1)

class graduateStudent(Student):
    def __init__(self, name, age, major):
        super().__init__(name, age, major)
    
    def introduce(self):
        return super().introduce()