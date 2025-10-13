a = int(input("Enter 1st no.: "))
b = int(input("Enter 2nd no.: "))
print("A") if a<b else print("=") if a==b else print("B")
c = 9 if a>b else 0
print(c)