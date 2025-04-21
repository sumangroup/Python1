class Employee:
    company='ABC Corp' # class variable

    def getInfo(self,name,emp_id,dept):
        self.name=name
        self.emp_id=emp_id
        self.dept=dept
        
    def printInfo(self):
        print(self.name)
        print(self.emp_id)
        print(self.dept)
     
emp1=Employee() # object creation
emp1.getInfo("Raju Mane",101,"CS")
emp1.printInfo()
print(emp1.company)

print()
emp2=Employee()
emp2.getInfo("Mrunali Prasade",102,"CS")
emp2.printInfo()
print(emp2.company)
