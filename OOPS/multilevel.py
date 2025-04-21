class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def displayperson(self):
        print(self.name)
        print(self.age)

class student(person):
    def __init__(self,name,age,rollno,major):
        super().__init__(name,age)
        self.rollno=rollno
        self.major=major

    def displaystudent(self):
        super().displayperson()
        print(self.rollno)
        print(self.major)

class sciencestudent(student):
    def __init__(self,name,age,rollno,major,specialization):
        super().__init__(name,age,rollno,major)
        self.specialization=specialization

    def displaysci(self):
        super().displaystudent()
        print(self.specialization)

science1 = sciencestudent("Priya Patel", 20, "SC405", "Science", "Biology")
science1.displaysci()














        
    

    
