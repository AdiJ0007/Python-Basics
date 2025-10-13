c = [1,2,3]
print(dir(c))
print(c.__add__,"\n")

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person("Shruti",19)
print(p.__dict__)

print(help(Person))