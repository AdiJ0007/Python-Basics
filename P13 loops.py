# For loop
# String
name = 'Aditya'
for i in name:
    print(i,end = ", ")
print("")

# List
colors = ["Red","Green","Blue","Yellow"]
for x in colors:
    print(x)
    # for i in x:
    #     print(i)
    
# range()
for m in range(10):
    print(m, end = ", ")
print("")
for m in range(1,9):
    print(m+1,end = ", ")
print("")
for m in range(0,21,5):  #3rd argument in range() function
    print(m)

# While loop
i = 0
while(i<5):
    print(i)
    i = i + 1
i = int(input("Enter a no.: "))
while(i > 20):
    i = int(input("Enter a no.: "))
    print(i)
count = 5
while(count > 0):
    print(count)
    count = count - 1
else:
    print("I am inside else")
