class Employee:
    company='ABC Corp' # class variable

    def __init__(self,name,emp_id,dept):
        self.name=name
        self.emp_id=emp_id
        self.dept=dept
        
    def printInfo(self):
        print(self.name)
        print(self.emp_id)
        print(self.dept)

    @classmethod
    def change_company(cls,new_company):
        cls.name=new_company
        print(cls.name)
     
emp1=Employee("Raju Mane",101,"CS") # object creation
emp1.printInfo()
print(emp1.company)

print()
emp2=Employee("Mrunali Prasade",102,"CS")

emp2.printInfo()
print(emp2.company)

# class method called
Employee.change_company('XYZ corp')
print(emp2.company)


