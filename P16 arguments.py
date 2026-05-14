# default arguments
def avg(a = 5, b = 7):
    print("Average is:",(a+b)/2)
avg()            #takes default arguments as input
avg(2,4)         #takes provided input
avg(4)
avg(b=3)


# keyword arguments
def Greater(a,b):
    if(a>b):
        print(a,"is greater than",b)
    elif(a==b):
        print("both are equal")
    else:
        print(b,"is grater than",a)
Greater(b=12,a=34)   #If this type of syntax is used,no order is required


# required arguments
def Car(fname,lname):
    print("Customized",fname,lname)
Car("Nissan","GT-R34")


# variable-length arguments
# arbitrary arguments
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print(sum/len(numbers))
average(2,4,6,8,10,12,14)

# keyword arbitrary arguments
def name(**name):
    print("Hello",name["fname"],name["mname"],name["lname"])
name(mname="Supra",lname="MkIV",fname="Toyota")


# return statement
def ave(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)
c = ave(2,4,6,8,10,12,14,16,18,20,22)
print(c)
