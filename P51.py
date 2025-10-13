class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
    def showDetails(self):
        print(f"The name of employee: {self.id} is {self.name}")
  
class Programmer(Employee):
    def showLanguages(self):
        print("The default language is Python")

e = Employee("Mohan Das",420)
e.showDetails()
e2 = Programmer("Rohan Das",421)
e2.showDetails()
e2.showLanguages()
e3 = Employee("Sohan Das",422)
e3.showDetails()
