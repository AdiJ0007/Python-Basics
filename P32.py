a = input("Enter a no. between 4 and 9(or you may quit): ")
if(a !='quit' and( int(a)<4 or int(a)>9)):
    raise ValueError("The no. must be between 4 and 9 or you may quit")
else:
    print("Accepted")