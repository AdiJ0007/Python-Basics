class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0
    
    def books1(self,book):
        self.books.append(book)
        self.no_of_books += 1
    
    def show(self):
        print("The books in Library are: ")
        for book in self.books:  
            print(book)
            
    def no(self):
        print(f"The total no. of books in Library are {self.no_of_books}")
     
    def check(self):
        if(len(self.books) != self.no_of_books):
            raise ValueError("The no. of books do not match")
        else:
            print("The no. of books in library are OK")
        
a = Library()
a.books1("Harry Potter and The Philosophers Stone")
# b = Library()
a.books1("Harry Potter and The Chamber of Secrets")
# c = Library()
a.books1("Harry Potter and The Prisoner Of Azkaban")
# d = Library()
a.books1("Harry Potter and The Goblet Of Fire")
# e = Library()
a.books1("Harry Potter and The Order Of The Phoenix")
# f = Library()
a.books1("Harry Potter and The Half Blood Prince")
# g = Library()
a.books1("Harry Potter and The Deathly Hallows")
print(a.show())
print(a.no())
print(a.check())