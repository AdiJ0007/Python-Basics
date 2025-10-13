a = int(input("Enter your age: "))
print("Your age is",a)
if(a>18):
    print("You can drive")
else:
    print("You cannot drive")
    
n = int(input("enter an integer: "))
if(n < 0):
    print("The no. is negative")
elif(n == 0):
    print("The no. is zero")
elif(n == 999):
    print("The no. is special")
else:
    print("The no. is positive")
    
m = int(input("Enter a no.: "))
if(m < 0):
    print("no. is negative")
elif(m > 0):
    print("no. is positive")
    if(m < 10):
        print("No. is less than 10")
    elif(m > 10 and m < 20):
        print("No. is between 10-20")
    else:
        print("No. is greater tha 20")
else:
    print("No. is zero")