class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display_details(self):
        print(self.name)
        print(self.rollno)

class UndergraduateStudent(student):
    def __init__(self,name,rollno,major):
        super().__init__(name,rollno)
        self.major=major

    def display_details(self):
        super().display_details()
        print(self.major)

std1=UndergraduateStudent("raju",101,"cs")
std1.display_details()
