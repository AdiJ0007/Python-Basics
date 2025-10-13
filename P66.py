class Employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")

class Sport:
    def __init__(self,sport):
        self.sport = sport
    def show(self):
        print(f"The sport is {self.sport}")

class Player_Employee(Employee,Sport):
    def __init__(self,sport,name):
        self.sport = sport
        self.name = name
    
a = Player_Employee("Football", "Bantu")
print(a.name)
print(a.sport)
a.show()
print(Player_Employee.mro())