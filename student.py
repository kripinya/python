class Student:
    def __init__(self, name, r_no, branch):
        self.name = name
        self.r_no = r_no
        self.branch = branch

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"roll number: {self.r_no}")
        print(f"branch: {self.branch}")
#creating object
s1 = Student("ananya", 500125205, "CSE")
s1.display_details()
