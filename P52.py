class Student:
    def __init__(self,name):
        self.name = name
        
a = Student("Yash")
print(a.name)
# print(a.__dir__())

class Employee:
    def __init__(self):
        self.__name = "Harsh"

b = Employee()
# print(b.__name)  #cannot access directly
print(b._Employee__name)   #indirectly accessing
# print(b.__dir__())

class Employer():
    def __init__(self):
        self._name = "Puneet"

c = Employer()
print(c._name)
print(c.__dir__())