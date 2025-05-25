class Student:
    def __init__(self, name, rollno, branch):
        self.__name = name
        self.__rollno = rollno
        self.__branch = branch

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_rollno(self):
        return self.__rollno

    def set_rollno(self, rollno):
        self.__rollno = rollno

    def get_branch(self):
        return self.__branch

    def set_branch(self, branch):  # ✅ Ensure this method exists
        self.__branch = branch

    def display_details(self):
        print(f"Name: {self.__name}")
        print(f"Roll No: {self.__rollno}")
        print(f"Branch: {self.__branch}")

s1 = Student("ananya", 500125205, "CSE")
s1.display_details()