class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

class Program:
    def __init__(self,program_name,duration):
        self.program_name = program_name
        self.duration = duration
        
    def show(self):
        print(f"Program_name : {self.program_name}")
        print(f"Duration: {self.duration}")

class Person(Human,Program):
    def __init__(self,name,age,address,program_name, duration):
        Human.__init__(self, name, age)
        Program.__init__(self, program_name, duration)
        self.address = address
    
    def show(self):
        Human.show(self)
        Program.show(self)
        print(f"Address : {self.address}")
    
class Student(Person):
  def __init__(self, name, age, address, program_name,duration):
    Person.__init__(self, name, age, address,program_name, duration)
    
        
  def show_details(self):
    Person.show(self)
    
       
student = Student("Sourabh", 20, "Times Square", "Electronics",4)
student.show()
