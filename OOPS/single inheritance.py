class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_person(self):
        print(self.name)
        print(self.age)

class Student(Person):

    def __init__(self,name,age,rollno,major):
        super().__init__(name,age)
        self.rollno=rollno
        self.major=major

    def displaystudent(self):
        super().display_person()
        print(self.rollno)
        print(self.major)


std1=Student("Raju Mane",32,101,"CS")
std1.displaystudent()

std2=Student("Mrunali Prasade",19,102,"CS")
std2.displaystudent()


    
        
