class Student:
    def __init__(self, name, r_no, branch, cgpa):
        self.name = name
        self.r_no = r_no
        self.branch = branch
        self.cgpa = cgpa

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.r_no}")
        print(f"Branch: {self.branch}")
        print(f"CGPA: {self.cgpa}")

class GraduateStudent(Student):
    def __init__(self, name, r_no, branch, degree, cgpa):
        super().__init__(name, r_no, branch, cgpa)  # ✅ Fixed super()
        self.degree = degree

    def display_details(self):
        super().display_details()  # ✅ Calls parent method
        print(f"Degree: {self.degree}")  # ✅ Fixed case

# ✅ Create object and test
g1 = GraduateStudent("Ananya", "U21CSE123", "CSE", "BTech", 9.0)
g1.display_details()