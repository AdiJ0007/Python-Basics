class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def show(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species = "Dog")
        self.breed = breed

    def show(self):
        Animal.show(self)
        print(f"Breed : {self.breed}")

class GoldenRetriever(Dog):
    def __init__(self,name,colour):
        Dog.__init__(self, name, breed = "Golden Retriever")
        self.colour = colour
    
    def show(self):
        Dog.show(self)
        print(f"Colour : {self.colour}")
        
E = GoldenRetriever("Entertainment", "Golden")
E.show()
print(GoldenRetriever.mro())