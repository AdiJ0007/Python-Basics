class Cars:
    def __init__(self, name, category):
        print("I Love Cars")
        self.name = name
        self.category = category
    
    def info(self):
        print(f"{self.name} is a {self.category}")

a = Cars("Pontiac Firebird","Muscle Car")
b = Cars("Shelby GT500","Muscle Car")
a.info()
b.info()