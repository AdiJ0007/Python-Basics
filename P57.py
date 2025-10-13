class Employee:
    company = "Porsche"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
    
    @classmethod
    def changeCompany(cls,newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Yash"
e1.show()
e1.changeCompany("Ford")
e1.show()
print(Employee.company)