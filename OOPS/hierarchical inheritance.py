class student:
    
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
    def displaystudent(self):
        print(self.name)
        print(self.rollno)

class UndergraduateStudent(student):

    def __init__(self,name,rollno,major):
        super().__init__(name,rollno)
        self.major=major

    def displayug(self):
        super().displaystudent()
        print(self.major)

class GraduateStudent(student):
    """Subclass representing a graduate student, inheriting from Student."""
    def __init__(self, name, rollno, research_topic):
        super().__init__(name, rollno)
        self.research_topic = research_topic

    def display_graduate_info(self):
        super().displaystudent()
        print(self.research_topic)

student1=UndergraduateStudent("Mrunali",45,"COMPS")
student1.displayug()

student2=GraduateStudent("Raju Mane",67,"AI")
student2.display_graduate_info()






