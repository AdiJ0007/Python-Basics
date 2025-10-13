try:
    l = [1,5,6,7]
    i = int(input("Enter any no: "))
    print(l[i])
except:
    print("Some error occured")
finally:
    print("I am always executed")
    
def alloy():
    try:
        wheel = [16,17,18,19,20]
        size = int(input("Enter a no.: "))
        print(wheel[size])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always executed")
x = alloy()
print(x)