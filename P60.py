class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang

Yash = Employee("Yash",7)
Harry = Programmer("Harry",420,"Nodejs")
print(Yash.name,Yash.id)
print(Harry.name,Harry.id,Harry.lang)

