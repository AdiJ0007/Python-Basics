def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return (n*factorial(n-1))
n = int(input("Enter a no.:"))
print(factorial(n))

# n1 = 0
# n2 = 1
# n3 = n1 + n2
# n = (n-1)+(n-2)
def fibonacci(a):
    x = 0
    y = 1
    print(x,y,end = " ")
    for a1 in range(1,a):
        a1 = a1+1
        z = x+y
        x = y
        y = z
        print(z,end = " ")
print(fibonacci(11))