class Employee:
    companyName = "Apple"
    noOfEmployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amt = 0.02
        Employee.noOfEmployees += 1
    
    def showDetails(self):
        print(f"Employee {self.name} of {self.companyName} sized {self.noOfEmployees} has a raise of {self.raise_amt}")
emp1 = Employee("Yash")
emp1.raise_amt = 0.3
emp1.companyName = "Google"
emp1.showDetails()
print(Employee.companyName)
Employee.companyName = "Apple India"
print(Employee.companyName)
emp2 = Employee("Harry")
emp2.showDetails()