class Cars:
    name = "2005 Ford Mustang GT"
    category = "Muscle car"
    worth = 18995
    def info(self):
        print(f"The car {self.name} is worth ${self.worth}")

a = Cars()
b = Cars()
c = Cars()
a.name = "Chevy Camaro"
a.worth = 32495
b.name = "1970 Dodge Charger r/t"
b.worth = 86200
# print(a.name,a.worth)
a.info()
b.info()
c.info()