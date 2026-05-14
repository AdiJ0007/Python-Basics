# Break statement
for i in range(12):
    if(i == 10):
        break
    print("5 X", i+1," =", 5*(i+1))

# Continue statement
for i in range(1,11,1):
    if(i == 5):
        continue
    print(i,i,"Supra")

# emulation of do-while loop in python
n = 0
while True:
    print(n)
    n = n+1
    if(n == 7):
        break
